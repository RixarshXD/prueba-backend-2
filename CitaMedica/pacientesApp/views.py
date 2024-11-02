from django.shortcuts import render, redirect
from .models import Pacientes
from .forms import FormPacientes
# Create your views here.

# Se crea la vista para el listado de pacientes.
# Se obtienen todos los pacientes de la base de datos y se envían al template 'ListadoPacientes.html'.
def listadoPacientes(request):
    pacientes = Pacientes.objects.all()
    data = {'pacientes': pacientes}
    return render(request,'Pacientes/listadoPacientes.html',data)

# Se crea la vista para registrar un paciente.
# Se crea un formulario vacío para registrar un paciente.
# Si el formulario es válido, se guarda el paciente en la base de datos y se redirige a la lista de pacientes.
def registroPacientes(request):
    form = FormPacientes()
    if request.method == 'POST':
        form = FormPacientes(request.POST)
        if form.is_valid():
            form.save()
            return listadoPacientes(request)
    data = {'form': form}
    return render(request,'Pacientes/registrarPacientes.html',data)

# Se crea la vista para eliminar un paciente.
# Se obtiene el paciente a eliminar y se elimina de la base de datos.
# Se redirige a la lista de pacientes.
def eliminarPacientes(request,id):
    pacientes = Pacientes.objects.get(id = id)
    pacientes.delete()
    return redirect('Pacientes/listadoPacientes')

# Se crea la vista para actualizar un paciente.
# Se obtiene el paciente a actualizar y se crea un formulario con los datos del paciente.
# Si el formulario es válido, se actualiza el paciente y se redirige a la lista de pacientes.
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