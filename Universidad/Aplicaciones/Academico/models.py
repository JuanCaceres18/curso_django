from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos =  models.PositiveSmallIntegerField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    curso = models.CharField(max_length=20)
    