from django.contrib import admin
from django.urls import path

from .views import listadoPacientes, registroPacientes

urlpatterns = [
    path('', listadoPacientes, name='pacientes'),
    path('registro/', registroPacientes, name='registro'),
]