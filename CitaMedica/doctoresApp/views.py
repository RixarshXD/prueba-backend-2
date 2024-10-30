from django.shortcuts import render
from .models import Doctor

# Create your views here.



# apartado doctores
def listadoDoctores(request):
    doctores = Doctor.objects.all()
    data = {'doctores': doctores}
    return render(request,'listadoDoctores.html', data)

def registroDoctores(request):
    return render(request,'registroDoctores.html')

def eliminarDoctores(request):
    return render(request,'eliminarDoctores.html')

def actualizarDoctores(request):
    return render(request,'actualizarDoctores.html')

