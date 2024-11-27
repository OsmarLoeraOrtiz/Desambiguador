from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Document, Requirement, Ambiguity, DisambiguationSuggestion, Proyecto
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages 

# Create your views here.
@login_required
def documentos(request):
    proyecto_id = request.session['id_proyecto']
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    documentos = Document.objects.filter(proyecto=proyecto).order_by('-uploaded_at')
    
    return render(request, 'documentos.html', {'documentos': documentos})

@login_required
def requisitos(request):
    proyecto_id = request.session['id_proyecto']
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    
    requisitos = Requirement.objects.filter(proyecto=proyecto).order_by('-created_at')
    
    return render(request, 'requisitos.html', {'requisitos': requisitos})


def proyectos(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        proyecto = Proyecto(nombre=nombre, descripcion=descripcion, user=request.user)
        proyecto.save() 
        
    proyectos = Proyecto.objects.filter(user=request.user).order_by('-created_at')
    context = {}
    print(proyectos)
    if proyectos:
        context = {
            'proyectos': proyectos
        }
    return render(request, 'proyectos.html', context)

def abrir_proyecto(request, id_proyecto):
    request.session['id_proyecto'] = id_proyecto
    return render(request, 'identificar_requisitos.html')

# Vista para eliminar un proyecto
def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    if request.method == "POST":  # Confirmación de eliminación
        nombre_proyecto = proyecto.nombre
        proyecto.delete()
        messages.success(request, f"El proyecto '{nombre_proyecto}' ha sido eliminado exitosamente.")
        return redirect("proyectos")  # Redirigir a la lista de proyectos
    return render(request, "proyectos.html", {"proyecto": proyecto})

# Vista para eliminar un documento
def eliminar_documento(request, documento_id):
    documento = get_object_or_404(Document, id=documento_id)
    if request.method == "POST":  # Confirmación de eliminación
        nombre_documento = documento.original_name or f"Documento #{documento.id}"
        documento.delete()
        messages.success(request, f"El documento '{nombre_documento}' ha sido eliminado exitosamente.")
        return redirect("documentos")  # Redirigir a la lista de documentos
    return render(request, "documentos.html", {"documento": documento})

def detalles_documento(request, documento_id):
    documento = get_object_or_404(Document, id=documento_id)
    return render(request, "detalles_documento.html", {"documento": documento})

def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        descripcion = request.POST.get("descripcion", "").strip()
        if nombre and descripcion:
            proyecto.nombre = nombre
            proyecto.descripcion = descripcion
            proyecto.save()
            return redirect("proyectos")  # Redirigir a la lista de proyectos (ajusta el nombre de la ruta según tu configuración)
    return render(request, "proyectos.html", {"proyecto": proyecto})