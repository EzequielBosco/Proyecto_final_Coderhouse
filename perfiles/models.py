from django.db import models

class Perfil(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=20)

    def __str__(self):
        return f"ID:{self.id}, Usuario:{self.nombre_usuario}, Correo:{self.email}"