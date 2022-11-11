from django.db import models
from django.contrib.auth.admin import User

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=30)
    sub_titulo = models.CharField(max_length=100)
    cuerpo = models.TextField(max_length=2000)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="imagenpost", null=True, blank=True)

    def __str__(self):
        return f"Id: {self.id}, Titulo: {self.titulo}, Autor: {self.autor}"

class Comentarios(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    nombre = models.CharField(max_length=20)
    correo = models.EmailField(max_length=50)
    mensaje = models.TextField(max_length=2000)
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return f"Id: {self.id}, Nombre: {self.nombre}, Fecha: {self.fecha}"