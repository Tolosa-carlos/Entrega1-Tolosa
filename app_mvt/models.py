from django.db import models

# Create your models here.

class Menu(models.Model):

    nombre = models.CharField(max_length=50)
    clase_comida = models.CharField(max_length=50) # Ej: Desayuno o almuerzo
    precio = models.IntegerField()

class Empleados(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()


class modelo3(models.Model):

    pass

