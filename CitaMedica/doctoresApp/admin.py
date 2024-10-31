from django.contrib import admin
from .models import Doctor

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'rut', 'fechaNacimiento', 'especialidad', 'correo')

admin.site.register(Doctor, DoctorAdmin)