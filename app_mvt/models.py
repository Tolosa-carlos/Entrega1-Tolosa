from django.db import models

# Create your models here.

class Menu(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()

class Empleados(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()



