from django.contrib import admin
from django.urls import path

from .views import listadoDoctores, registrarDoctores

urlpatterns = [
    path('', listadoDoctores, name='doctores'),
    path('registro/', registrarDoctores, name='registro/doctores'),
]