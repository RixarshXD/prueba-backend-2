from django.contrib import admin
from .models import Cita

# Register your models here.

class CitaAdmin(admin.ModelAdmin):
    list_display = ('fechaCita', 'diagnostico', 'horaCita', 'motivo', 'observacion', 'doctor', 'paciente')

admin.site.register(Cita, CitaAdmin)