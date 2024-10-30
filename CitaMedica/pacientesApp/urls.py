from django.contrib import admin
from django.urls import path

from .views import listadoPacientes, registroPacientes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listadoPacientes, name='pacientes'),
    path('registro/', registroPacientes, name='registro'),
]