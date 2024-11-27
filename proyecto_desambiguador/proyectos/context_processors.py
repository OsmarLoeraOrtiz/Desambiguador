# myapp/context_processors.py
from .models import Proyecto, Document

def obtener_datos_proyecto(request):
    # Verifica si hay un proyecto activo en la sesión o en otra variable
    try:
        proyecto_id = request.session["id_proyecto"]
    except KeyError:
        proyecto_id = None
        
    if proyecto_id:
        try:
            proyecto = Proyecto.objects.get(id=proyecto_id)
            documentos = Document.objects.filter(proyecto=proyecto)
            return {
                "proyecto_activo": proyecto,
                "documentos_proyecto": documentos,
                "proyecto_nombre": proyecto.nombre,
            }
        except Proyecto.DoesNotExist:
            return {}
    return {}
