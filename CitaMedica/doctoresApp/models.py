from django.db import models

# Create your models here.

class Doctor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.IntegerField()
    fechaNacimiento = models.DateField()
    especialidad = models.CharField(max_length=50)
    correo = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
   