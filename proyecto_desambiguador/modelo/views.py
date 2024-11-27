from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from proyectos.models import Document, Requirement, Ambiguity, DisambiguationSuggestion, Proyecto
import PyPDF2
import google.generativeai as genai
import json


import json
import PyPDF2

# Extraer texto de un archivo PDF
def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            extracted_text = ""
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    extracted_text += text.encode('utf-8').decode('utf-8')
            return extracted_text
    except Exception as e:
        print(f"Error al extraer texto del PDF: {e}")
        return None


# Generar el prompt de validación
def generar_prompt_validacion(texto):
    validacion_inicial = """
    Regresa el texto legible y sin errores ortográficos de los requisitos de software que están en el texto en el siguiente formato y en una sola línea:
    
    texto del requisito 1
    texto del requisito 2
    ...
    texto del requisito n
    
    Si el texto no contiene ningún requisito, deja de analizar el texto y responde exactamente con el número: 0
    Analiza el siguiente texto y proporciona la salida según las instrucciones anteriores:
    """
    return validacion_inicial + "\n\n" + texto

def generar_prompt_ambiguedad(texto):
    ambiguedad_inicial = """
    Analiza si los siguientes requisitos de software contienen palabras con mas de un sentido en base al contexto y/o las frases que tengan mas de una estructura gramatical.
    
    Si el requisito no tiene ambiguiedad, no lo muestres. Si tiene ambiguedad responde con la/s palabras o frases que tienen ambiguedad y una breve descripcion.
    formato de salida:
    id de requisito,palabra o frase con ambiguedad - descripcion de la ambiguedad.
    """
    return ambiguedad_inicial + "\n\n" + texto
# Procesar requisitos del texto de entrada
def procesar_requisitos(texto, documento, proyecto):
    try:
        requisitos_procesados = []
        
        # Procesar cada línea del texto
        for req_texto in texto.splitlines():
            req_texto = req_texto.strip()  # Eliminar espacios en blanco alrededor

            if req_texto:  # Solo procesar textos no vacíos
                # Crear un nuevo requisito en la base de datos
                requisito = Requirement.objects.create(
                    proyecto=proyecto,
                    document=documento,
                    text=req_texto,  # Guardamos el texto del requisito
                )
                requisitos_procesados.append({
                    'id': requisito.id,
                    'texto': requisito.text
                })

        return requisitos_procesados

    except Exception as e:
        print(f"Error al procesar los requisitos: {e}")
        return []



# Procesar ambigüedades del JSON devuelto
def procesar_ambiguedades(respuesta_prompt):
    """
    Procesa la salida del prompt para identificar y guardar ambigüedades en el modelo Ambiguity.
    
    Args:
        respuesta_prompt (str): Salida del prompt en el formato:
            "id de requisito,palabra o frase con ambiguedad - descripcion de la ambiguedad"
            

    Returns:
        list: Lista de ambigüedades guardadas o un mensaje indicando que no hay ambigüedades.
    """
    ambiguedades_guardadas = []

    try:
        # Dividir la respuesta en líneas para procesar cada ambigüedad
        lineas = respuesta_prompt.strip().split("\n")
        for linea in lineas:
            partes = linea.split(",", 1)
            print(partes)  # Dividir en ID y el resto del texto
            if len(partes) < 2:
                continue  # Saltar líneas mal formateadas
            
            req_id = partes[0].strip()  # ID del requisito
            ambiguedad_descripcion = partes[1].strip()  # Descripción de la ambigüedad

            # Buscar el requisito en la base de datos
            try:
                requisito = Requirement.objects.get(id=req_id)
            except Requirement.DoesNotExist:
                print(f"Requisito con ID {req_id} no encontrado.")
                continue

            # Crear y guardar la ambigüedad
            ambiguedad = Ambiguity.objects.create(
                requirement=requisito,
                description=ambiguedad_descripcion,
                detected_at=timezone.now()
            )
            ambiguedades_guardadas.append({
                "id": ambiguedad.id,
                "requirement_id": requisito.id,
                "requirement_text": requisito.text,
                "description": ambiguedad.description,
            })

        return ambiguedades_guardadas

    except Exception as e:
        print(f"Error al procesar ambigüedades: {e}")
        return f"Error al procesar ambigüedades: {e}"



# Vista para identificar requisitos
@login_required
def identificar_requisitos(request):
    
    proyecto_id = request.session['id_proyecto']
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    requisitos_validos = {}

    if request.method == "POST":
        texto_requisitos = request.POST.get('requisitos_texto', '').strip()
        archivo = request.FILES.get('requisitos_archivo')

        if texto_requisitos:
            documento = Document.objects.create(proyecto=proyecto, original_name="Texto manual", texto_manual=texto_requisitos)
            prompt_validacion = generar_prompt_validacion(texto_requisitos)
        elif archivo and archivo.content_type == 'application/pdf':
            documento = Document.objects.create(proyecto=proyecto, file=archivo, original_name=archivo.name)
            texto_extraido = extract_text_from_pdf(documento.file.path)
            if not texto_extraido:
                messages.error(request, "No se pudo extraer texto del archivo PDF.")
                return render(request, 'identificar_requisitos.html')
            prompt_validacion = generar_prompt_validacion(texto_extraido)
        else:
            messages.error(request, "Por favor, proporciona un texto o un archivo PDF válido.")
            return render(request, 'identificar_requisitos.html')

        # Validar requisitos
        genai.configure(api_key="AIzaSyATWFJFyhguScg6T0M1CeBj8hlu6Qpg4EQ")
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response_validacion = model.generate_content(prompt_validacion)
        print(response_validacion.text)

        if response_validacion.text.strip() == "0":
            messages.error(request, "La entrada proporcionada no contiene requisitos válidos.")
        else:
            requisitos_validos = procesar_requisitos(response_validacion.text, documento, proyecto)
            

    return render(request, 'identificar_requisitos.html', {'requisitos': requisitos_validos})


# Vista para detectar ambigüedades
@login_required
def detectar_ambiguedades(request):
    resultado = {}
    genai.configure(api_key="AIzaSyATWFJFyhguScg6T0M1CeBj8hlu6Qpg4EQ")

    proyecto_id = request.session['id_proyecto']
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    documentos = Document.objects.filter(proyecto=proyecto).order_by('-uploaded_at')

    if request.method == "POST":
        documento_id = request.POST.get('documento')
        documento = Document.objects.get(id=documento_id)
        requisitos = Requirement.objects.filter(document=documento)

        if not requisitos.exists():
            messages.error(request, "No se encontraron requisitos asociados al documento seleccionado.")
            return render(request, 'detectar_ambiguedades.html', {'documentos': documentos})
        texto_requisitos=""
        for requisito in requisitos:
            texto_requisitos += f"{requisito.id} {requisito.text}"
            
        prompt_ambiguedad = generar_prompt_ambiguedad(texto_requisitos)

        # Modelo ajustado para ambigüedades léxicas
        model_lexica = genai.GenerativeModel(model_name="tunedModels/elsujeto-edbj9h3si2ku")
        response_lexica = model_lexica.generate_content(prompt_ambiguedad)
        print(response_lexica.text)

        resultado = procesar_ambiguedades(response_lexica.text)
        print(resultado)

    return render(request, 'detectar_ambiguedades.html', {'documentos': documentos, 'resultado': resultado})
