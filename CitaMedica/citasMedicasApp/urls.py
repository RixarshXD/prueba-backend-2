from django.contrib import admin
from django.urls import path

from .views import listaCitas, registroCita, eliminarCita, modificarCita

urlpatterns = [
    path('', listaCitas, name='listaCitas'),
    path('registro/', registroCita, name='registro/citas'),
    path('eliminarCita/<int:id>/', eliminarCita, name='eliminarCita'),
    path('modificarCita/<int:id>/', modificarCita, name='modificarCita'),
]