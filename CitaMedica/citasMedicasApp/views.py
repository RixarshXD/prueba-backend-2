from django.shortcuts import render, redirect
from .models import Pacientes, Doctor, Cita
from ..pacientesApp.forms import FormPacientes

# Create your views here.

def index(request):
    return render(request,'index.html')


