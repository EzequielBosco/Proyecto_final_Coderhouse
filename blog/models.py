from django.db import models

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14)
    titulo_blog = models.CharField(max_length=20)
    subtitulo_blog = models.CharField(max_length=30)
    desarrollado_por = models.CharField(max_length=30)
