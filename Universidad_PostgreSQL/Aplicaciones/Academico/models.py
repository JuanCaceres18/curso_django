from django.db import models
from .choices import sexos

# Create your models here.
class Docente(models.Model):
    apellido_paterno = models.CharField(max_length=20, verbose_name='Apellido Paterno')
    apellido_materno = models.CharField(max_length=20, verbose_name='Apellido Materno')
    nombres = models.CharField(max_length=20, verbose_name='Nombres')
    fecha_nacimiento = models.DateField(verbose_name= "Fecha de Nacimiento")
    sexo = models.CharField(max_length=1, choices=sexos, default='F')

    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombres)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        db_table = 'docente'
        ordering = ['apellido_paterno', '-apellido_materno']
    

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos =  models.PositiveSmallIntegerField()
    docente = models.ForeignKey(Docente, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        text = '{0} ({1})'
        return text.format(self.nombre, self.creditos)