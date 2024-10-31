from django.db import models

# Create your models here.

class Pacientes(models.Model):
    nombre =models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.IntegerField()
    fechaNacimiento = models.DateField()
    correo =models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
   