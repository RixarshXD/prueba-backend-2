from django.shortcuts import render, redirect
from .models import Pacientes
from .forms import FormPacientes
# Create your views here.

# apartado pacientes
def listadoPacientes(request):
    pacientes = Pacientes.objects.all()
    data = {'pacientes': pacientes}
    return render(request,'Pacientes/listadoPacientes.html',data)

def registroPacientes(request):
    form = FormPacientes()
    if request.method == 'POST':
        form = FormPacientes(request.POST)
        if form.is_valid():
            form.save()
            return listadoPacientes(request)
    data = {'form': form}
    return render(request,'Pacientes/registrarPacientes.html',data)


def eliminarPacientes(request,id):
    pacientes = Pacientes.objects.get(id = id)
    pacientes.delete()
    return redirect('Pacientes/listadoPacientes')


def modificarPaciente(request,id):
    pacientes = Pacientes.objects.get(id=id)
    form = FormPacientes(instance=pacientes)
    if request.method == 'POST':
        form = FormPacientes(request.POST, instance=pacientes)
        if form.is_valid():
            form.save()
            return listadoPacientes(request)
    data = {'form': form}
    return render(request,'Pacientes/registrarPacientes.html',data)