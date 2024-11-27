from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proyecto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="proyectos", verbose_name="Usuario")
    nombre = models.CharField("Nombre del Proyecto", max_length=255)
    descripcion = models.CharField("Descripcion del Proyecto", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Document(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="documents", verbose_name="Proyecto")
    file = models.FileField(upload_to="documents/", help_text="Archivo del documento de requisitos", blank=True, null=True)
    archivo_resaltado = models.FileField(upload_to="documentos_resaltados/", help_text="Archivo del documento de requisitos resaltado", blank=True, null=True)
    original_name = models.CharField("Nombre del archivo original", max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    texto_manual = models.TextField(blank=True, null=True) 
    def __str__(self):
        return self.original_name if self.original_name else f"Documento #{self.id}"


class Requirement(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="requirements", verbose_name="Proyecto")
    document = models.ForeignKey(Document, on_delete=models.SET_NULL, related_name="requirements", blank=True, null=True)
    text = models.TextField("Texto del requisito", help_text="Texto completo del requisito ingresado")    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Requisito #{self.id}"


class Ambiguity(models.Model):
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name="ambiguities")
    description = models.TextField("Palabras clave ambiguas", help_text="Palabras o frases que causan la ambigüedad", null=True)
    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ambigüedad {self.type} en Requisito #{self.requirement.id}"

class DisambiguationSuggestion(models.Model):
    ambiguity = models.ForeignKey(Ambiguity, on_delete=models.CASCADE, related_name="suggestions")
    suggestion_text = models.TextField("Sugerencia de desambiguación", help_text="Texto que propone una solución para la ambigüedad")

    def __str__(self):
        return f"Sugerencia para Ambigüedad #{self.ambiguity.id}"