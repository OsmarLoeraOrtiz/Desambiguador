from django.conf import settings
import fitz  # PyMuPDF
import os
from typing import Dict, List
from datetime import datetime
import logging
import re

class PDFHighlighter:
    def __init__(self):
        self.colors = {
            'requisito': {'stroke': (1, 0.95, 0.4), 'fill': (1, 0.95, 0.4, 0.3)},  # Amarillo
            'lexica': {'stroke': (1, 0.4, 0.4), 'fill': (1, 0.4, 0.4, 0.3)},      # Rojo
            'sintactica': {'stroke': (0.4, 1, 0.4), 'fill': (0.4, 1, 0.4, 0.3)},  # Verde
            'semantica': {'stroke': (0.4, 0.4, 1), 'fill': (0.4, 0.4, 1, 0.3)}    # Azul
        }
        self.stats = {
            'requisitos_encontrados': 0,
            'requisitos_resaltados': 0,
            'ambiguedades_encontradas': 0,
            'ambiguedades_resaltadas': 0,
            'paginas_procesadas': 0
        }

    def generar_nombre_archivo(self, nombre_original: str) -> str:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        nombre_base, extension = os.path.splitext(nombre_original)
        return f"{nombre_base}_resaltado_{timestamp}{extension}"

    def resaltar_pdf(self, documento, resultado: Dict) -> str:
        """
        Resalta requisitos y ambigüedades en el PDF y devuelve la ruta del nuevo archivo.
        """
        try:
            pdf_path = documento.file.path
            doc = fitz.open(pdf_path)
            print(f"Procesando PDF: {pdf_path}")
            
            # Resetear estadísticas
            self.stats = {key: 0 for key in self.stats}
            
            # Preparar el texto completo del PDF para búsqueda
            texto_completo = ""
            for page in doc:
                texto_completo += page.get_text()
            
            # Procesar requisitos y ambigüedades
            for req_data in resultado.get('requisitos', []):
                self.stats['requisitos_encontrados'] += 1
                requisito = req_data['requisito']
                texto_req = requisito.text.strip()
                
                print(f"\nProcesando Requisito ID: {requisito.id_req_doc}")
                print(f"Texto del requisito: {texto_req}")
                
                # Verificar si el requisito está en el PDF
                if texto_req in texto_completo:
                    print(f"Requisito encontrado en el documento")
                    # Resaltar en todas las páginas donde aparezca
                    for page_num in range(len(doc)):
                        page = doc[page_num]
                        if self._resaltar_texto(page, texto_req, 'requisito', f"Requisito ID: {requisito.id_req_doc}"):
                            self.stats['requisitos_resaltados'] += 1
                else:
                    print(f"⚠️ Requisito no encontrado en el documento: {texto_req[:50]}...")
                
                # Procesar ambigüedades del requisito
                for amb_data in req_data['ambiguedades']:
                    self.stats['ambiguedades_encontradas'] += 1
                    ambiguedad = amb_data['ambiguedad']
                    
                    print(f"\nProcesando Ambigüedad Tipo: {ambiguedad.type}")
                    print(f"Descripción: {ambiguedad.description}")
                    
                    # Procesar keywords de la ambigüedad
                    if hasattr(ambiguedad, 'keywords') and ambiguedad.keywords:
                        keywords = ambiguedad.keywords if isinstance(ambiguedad.keywords, str) else ','.join(ambiguedad.keywords)
                        for keyword in keywords.split(','):
                            keyword = keyword.strip()
                            if not keyword:
                                continue
                                
                            print(f"Procesando keyword: {keyword}")
                            if keyword in texto_completo:
                                for page_num in range(len(doc)):
                                    page = doc[page_num]
                                    if self._resaltar_texto(
                                        page, 
                                        keyword,
                                        ambiguedad.type.lower(),
                                        f"Ambigüedad {ambiguedad.type}: {ambiguedad.description}"
                                    ):
                                        self.stats['ambiguedades_resaltadas'] += 1
                            else:
                                print(f"⚠️ Keyword no encontrada en el documento: {keyword}")

            # Generar y guardar el PDF resaltado
            nombre_resaltado = self.generar_nombre_archivo(documento.original_name)
            ruta_resaltado = os.path.join(settings.MEDIA_ROOT, 'documentos_resaltados', nombre_resaltado)
            os.makedirs(os.path.dirname(ruta_resaltado), exist_ok=True)
            
            doc.save(ruta_resaltado)
            doc.close()
            
            # Imprimir estadísticas
            print("\nEstadísticas de procesamiento:")
            print(f"Requisitos encontrados: {self.stats['requisitos_encontrados']}")
            print(f"Requisitos resaltados: {self.stats['requisitos_resaltados']}")
            print(f"Ambigüedades encontradas: {self.stats['ambiguedades_encontradas']}")
            print(f"Ambigüedades resaltadas: {self.stats['ambiguedades_resaltadas']}")
            
            return f"documentos_resaltados/{nombre_resaltado}"

        except Exception as e:
            print(f"Error al resaltar PDF: {str(e)}")
            if 'doc' in locals():
                doc.close()
            return None
    def _resaltar_texto(self, page, texto: str, tipo: str, nota: str = None) -> bool:
        """
        Subraya el texto con la coincidencia más cercana en una página.
        Retorna True si se realizó al menos un subrayado o resaltado.
        """
        try:
            if not texto or not isinstance(texto, str):
                print(f"⚠️ Texto inválido para subrayar: {texto}")
                return False
            
            if tipo not in self.colors:
                print(f"⚠️ Tipo de subrayado no válido: {tipo}")
                return False
            
            # Crear un patrón de búsqueda tolerante a espacios o saltos de línea
            # Dividimos el texto en palabras y permitimos cualquier cantidad de espacios o saltos de línea entre ellas.
            pattern = r"\s+".join(re.escape(word) for word in texto.split())
            text_instances = page.search_for(pattern, hit_max=16)

            if not text_instances:
                return False
            
            # Marcar con subrayado y resaltar las coincidencias que más se asemejen al texto original
            for inst in text_instances:
                # Crear subrayado
                underline = page.add_underline_annot(inst)
                underline.set_colors(
                    stroke=self.colors[tipo]['stroke'],
                    fill=self.colors[tipo]['fill']
                )
                
                # Agregar nota si se proporciona
                if nota:
                    text_annot = page.add_text_annot(
                        inst.tl,  # Punto superior izquierdo
                        nota
                    )
                
                underline.update()
            
            return len(text_instances) > 0
        
        except Exception as e:
            print(f"Error al subrayar texto '{texto}': {str(e)}")
            return False


def buscar_y_resaltar_requisitos(documento, resultado):
    """
    Función principal para procesar el PDF y resaltar requisitos y ambigüedades.
    """
    try:
        highlighter = PDFHighlighter()
        ruta_archivo_resaltado = highlighter.resaltar_pdf(documento, resultado)
        return ruta_archivo_resaltado
    except Exception as e:
        print(f"Error en el proceso de resaltado: {str(e)}")
        return None