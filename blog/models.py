from django.db import models

class Configuracion(models.Model):
    titulo = models.CharField(max_length=20)
    sub_titulo = models.CharField(max_length=30)