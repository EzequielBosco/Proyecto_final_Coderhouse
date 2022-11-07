from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=30)
    sub_titulo = models.CharField(max_length=100)
    cuerpo = models.TextField(max_length=2000)
    autor = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="imagenpost", null=True, blank=True)

    def __str__(self):
        return f"Id: {self.id}, Titulo: {self.titulo},   Autor: {self.autor}"