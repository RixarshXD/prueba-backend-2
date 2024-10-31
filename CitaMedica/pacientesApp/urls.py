from django.contrib import admin
from django.urls import path

from .views import listadoPacientes, registroPacientes, eliminarPacientes

urlpatterns = [
    path('', listadoPacientes, name='ListadoPacientes'),
    path('registro/', registroPacientes, name='registro/pacientes'),
    path('eliminarPaciente/<int:id>/',eliminarPacientes, name='eliminarPaciente/pacientes')
]