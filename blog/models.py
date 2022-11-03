from django.db import models

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14)
    titulo_blog = models.CharField(max_length=20)
    subtitulo_blog = models.CharField(max_length=30)
    desarrollado_por = models.CharField(max_length=30)

class Blog_post(models.Model):
    titulo = models.CharField(max_length=25)
    sub_titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=20)
    fecha = models.CharField(max_length=15)
    sub_titulo_1 = models.CharField(max_length=40)
    cuerpo = models.CharField(max_length=1000)
    imagen = models.CharField(max_length=15)
    cuerpo_1 = models.CharField(max_length=700)

class Blog(models.Model):
    titulo = models.CharField(max_length=25)
    sub_titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=20)
    fecha = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.titulo}, {self.sub_titulo}, {self.autor}, {self.fecha}"