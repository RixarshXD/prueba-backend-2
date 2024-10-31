from django.db import models
from doctoresApp.models import Doctor
from pacientesApp.models import Pacientes

# Create your models here.

class Cita(models.Model):
    fechaCita = models.DateTimeField()
    diagnostico = models.CharField(max_length=50)
    horaCita = models.TimeField()
    motivo = models.CharField(max_length=50)
    observacion = models.CharField(max_length=50)
        
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Pacientes, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'''{self.fechaCita} - {self.diagnostico} - {self.horaCita} - {self.motivo} - {self.observacion} - {self.doctor} - {self.paciente}'''
   