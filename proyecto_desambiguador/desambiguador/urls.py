
from django.contrib import admin
from django.urls import path, include
from autenticacion.views import principal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', principal, name='home'),
    path('autenticacion/', include('autenticacion.urls')),
    path('proyectos/', include('proyectos.urls')),
] 
