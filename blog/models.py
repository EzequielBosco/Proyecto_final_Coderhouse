from django.db import models

class ConfigIndex(models.Model):
    titulo = models.CharField(max_length=20)
    sub_titulo = models.CharField(max_length=30)
    sub_titulo_1 = models.CharField(max_length=30)

class Contacto(models.Model):
    nombre = models.CharField(max_length=20)
    correo = models.EmailField(max_length=50)
    numero_telefono = models.CharField(max_length=20)
    mensaje = models.TextField(max_length=2000)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Fecha: {self.fecha}"

class Comentario(models.Model):
    nombre = models.CharField(max_length=20)
    mensaje = models.TextField(max_length=2000)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Fecha: {self.fecha}"