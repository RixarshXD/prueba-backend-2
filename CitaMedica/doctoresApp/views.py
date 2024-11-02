from django.shortcuts import render, redirect
from .models import Doctor
from .forms import FormDoctor


# Se crea la vista para el listado de doctores.
# Se obtienen todos los doctores de la base de datos y se envían al template 'listadoDoctores.html'.
def listadoDoctores(request):
    doctores = Doctor.objects.all()
    data = {'doctores': doctores}
    return render(request,'Doctores/listadoDoctores.html', data)

# Se crea la vista para registrar un doctor.
# Se crea un formulario vacío para registrar un doctor.
# Si el formulario es válido, se guarda el doctor en la base de datos y se redirige a la lista de doctores.
def registrarDoctores(request):
    form = FormDoctor()
    if request.method == 'POST':
        form = FormDoctor(request.POST)
        if form.is_valid():
            form.save()
            return listadoDoctores(request)
    data = {'form': form}
    return render(request,'Doctores/registrarDoctores.html', data)

# Se crea la vista para eliminar un doctor.
# Se obtiene el doctor a eliminar y se elimina de la base de datos.
# Se redirige a la lista de doctores.
def eliminarDoctores(request, id):
    doctores = Doctor.objects.get(id = id)
    doctores.delete()
    return redirect('ListaDoctores')

# Se crea la vista para actualizar un doctor.
# Se obtiene el doctor a actualizar y se crea un formulario con los datos del doctor.
# Si el formulario es válido, se actualiza el doctor y se redirige a la lista de doctores.
def ModificarDoctores(request, id):
    doctores = Doctor.objects.get(id=id)
    form = FormDoctor(instance=doctores)
    if request.method == 'POST':
        form = FormDoctor(request.POST, instance=doctores)
        if form.is_valid():
            form.save()
            return listadoDoctores(request)
    data = {'form': form}
    return render(request,'Doctores/registrarDoctores.html', data)

