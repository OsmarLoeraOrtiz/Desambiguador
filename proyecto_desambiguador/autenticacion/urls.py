
from django.urls import path, include

from autenticacion.views import ingreso, registro, configuracion, salir

urlpatterns = [
    path('ingreso', ingreso, name='ingreso'),
    path('registro', registro, name='registro'),
    path('configuracion', configuracion, name='configuracion'),
    path('salir', salir, name='salir'),
]
