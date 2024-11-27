
from django.urls import path
from .views import  documentos, requisitos, proyectos, abrir_proyecto, detalles_documento, eliminar_documento
from django.conf import settings
from modelo.views import  identificar_requisitos, detectar_ambiguedades

urlpatterns = [
    path('documentos', documentos, name='documentos'),
    path('detalles_documento/<int:id_documento>/', detalles_documento, name='detalles_documento'),
    path('eliminar_documento/<int:id_documento>/', eliminar_documento, name='eliminar_documento'),
    path('requisitos', requisitos, name='requisitos'),
    path('', proyectos, name='proyectos'),
    path('abrir_proyecto/<int:id_proyecto>/', abrir_proyecto, name='abrir_proyecto'),
    path('identificar_requisitos', identificar_requisitos, name='identificar_requisitos'),
    path('procesar_ambiguedades', detectar_ambiguedades, name='procesar_ambiguedades'),
]