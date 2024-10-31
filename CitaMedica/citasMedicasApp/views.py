from django.shortcuts import render, redirect
from .models import Cita
from .forms import FormCitas


# Create your views here.

def index(request):
    return render(request,'index.html')


def listaCitas(request):
    cita = Cita.objects.all()
    data = {'cita': cita}
    return render(request,'CitasMedicas/listadoCitasMedicas.html',data)

def registroCita(request):
    form = FormCitas()
    if request.method == 'POST':
        form = FormCitas(request.POST)
        if form.is_valid():
            form.save()
            return listaCitas(request)
    data = {'form': form}
    return render(request,'CitasMedicas/registrarCitaMedica.html',data)

def eliminarCita(request,id):
    cita = Cita.objects.get(id = id)
    cita.delete()
    
    # se hace la referencia de la url en el archivo urls.py
    return redirect('listaCitas')

def modificarCita(request,id):
    cita = Cita.objects.get(id = id)
    form = FormCitas(instance = cita)
    if request.method == 'POST':
        form = FormCitas(request.POST, instance = cita)
        if form.is_valid():
            form.save()
            return listaCitas(request)
    data = {'form': form}
    return render(request,'CitasMedicas/registrarCitaMedica.html',data)