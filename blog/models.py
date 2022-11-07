from django.db import models

class ConfigIndex(models.Model):
    titulo = models.CharField(max_length=20)
    sub_titulo = models.CharField(max_length=30)
    sub_titulo_1 = models.CharField(max_length=30)
    
class ConfigAbout(models.Model):
    titulo = models.CharField(max_length=20)
    sub_titulo = models.CharField(max_length=30)
    
class ConfigContact(models.Model):
    titulo = models.CharField(max_length=20)
    sub_titulo = models.CharField(max_length=30)