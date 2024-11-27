# Generated by Django 4.2.5 on 2024-11-09 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiguity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='Tipo de ambigüedad detectada', max_length=50, verbose_name='Tipo de ambigüedad')),
                ('description', models.TextField(help_text='Descripción de la ambigüedad detectada', verbose_name='Descripción de la ambigüedad')),
                ('keywords', models.JSONField(help_text='Palabras o frases que causan la ambigüedad', null=True, verbose_name='Palabras clave ambiguas')),
                ('severity', models.CharField(help_text='Gravedad de la ambigüedad', max_length=50, verbose_name='Gravedad')),
                ('impact', models.TextField(help_text='Descripción del posible impacto en el desarrollo', verbose_name='Impacto')),
                ('location', models.CharField(help_text='Posición en el texto o en el documento', max_length=100, verbose_name='Ubicación en el requisito')),
                ('detected_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(help_text='Archivo del documento de requisitos', upload_to='documents/')),
                ('original_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre del archivo original')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del Proyecto')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripcion del Proyecto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Texto completo del requisito ingresado', verbose_name='Texto del requisito')),
                ('tipo', models.CharField(help_text='Funcional o No Funcional', max_length=50, verbose_name='Tipo de requisito')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requirements', to='proyectos.document')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='proyectos.proyecto', verbose_name='Proyecto')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='proyectos.proyecto', verbose_name='Proyecto'),
        ),
        migrations.CreateModel(
            name='DisambiguationSuggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion_text', models.TextField(help_text='Texto que propone una solución para la ambigüedad', verbose_name='Sugerencia de desambiguación')),
                ('justification', models.TextField(help_text='Explicación de por qué la propuesta resuelve la ambigüedad', verbose_name='Justificación')),
                ('ambiguity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggestions', to='proyectos.ambiguity')),
            ],
        ),
        migrations.AddField(
            model_name='ambiguity',
            name='requirement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ambiguities', to='proyectos.requirement'),
        ),
    ]
