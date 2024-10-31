from django.contrib import admin
from django.urls import path

from .views import listaCitas, registroCita

urlpatterns = [
    path('', listaCitas, name='listaCitas'),
    path('registro/', registroCita, name='registro/citas'),
]