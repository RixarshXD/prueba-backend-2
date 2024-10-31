from django.contrib import admin
from django.urls import path

from .views import listadoDoctores, registrarDoctores, eliminarDoctores

urlpatterns = [
    path('', listadoDoctores, name='ListaDoctores'),
    path('registro/', registrarDoctores, name='registro/doctores'),
    path('eliminarDoctor/<int:id>/', eliminarDoctores, name='eliminarDoctor')
]