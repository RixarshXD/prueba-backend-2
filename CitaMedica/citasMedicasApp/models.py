from django.db import models

# Create your models here.

class Cita(models.Model):
    fechaCita = models.DateTimeField()
    diagnostico = models.CharField(max_length=50)
    horaCita = models.DateTimeField()
    motivo = models.CharField(max_length=50)
    observacion = models.CharField(max_length=50)
    
    