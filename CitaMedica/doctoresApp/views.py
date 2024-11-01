from django.shortcuts import render, redirect
from .models import Doctor
from .forms import FormDoctor

# Create your views here.

def listadoDoctores(request):
    doctores = Doctor.objects.all()
    data = {'doctores': doctores}
    return render(request,'Doctores/listadoDoctores.html', data)

def registrarDoctores(request):
    form = FormDoctor()
    if request.method == 'POST':
        form = FormDoctor(request.POST)
        if form.is_valid():
            form.save()
            return listadoDoctores(request)
    data = {'form': form}
    return render(request,'Doctores/registrarDoctores.html', data)


def eliminarDoctores(request, id):
    doctores = Doctor.objects.get(id = id)
    doctores.delete()
    return redirect('ListaDoctores')

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

