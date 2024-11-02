from django.shortcuts import render, redirect
from .models import Cita
from .forms import FormCitas


#Función para la página de inicio
def index(request):
    return render(request,'index.html')

#Se crea la vista para el listado de citas.
#Se obtienen todas las citas de la base de datos y se envían al template 'listadoCitasMedicas.html'.
def listaCitas(request):
    cita = Cita.objects.all()
    data = {'cita': cita}
    return render(request,'CitasMedicas/listadoCitasMedicas.html',data)

#Se crea la vista para registrar una cita.
#Se crea un formulario vacío para registrar una cita.
#Si el formulario es válido, se guarda la cita en la base de datos y se redirige a la lista de citas.
def registroCita(request):
    form = FormCitas()
    if request.method == 'POST':
        form = FormCitas(request.POST)
        if form.is_valid():
            form.save()
            return listaCitas(request)
    data = {'form': form}
    return render(request,'CitasMedicas/registrarCitaMedica.html',data)

#Se crea la vista para eliminar una cita.
#Se obtiene la cita a eliminar y se elimina de la base de datos.
#Se redirige a la lista de citas.
def eliminarCita(request,id):
    cita = Cita.objects.get(id = id)
    cita.delete()
    
    #Se hace la referencia de la url en el archivo "urls.py".
    return redirect('listaCitas')

#Se crea la vista para modificar una cita.
#Se obtiene la cita a modificar y se crea un formulario con los datos de la cita.
#Si el formulario es válido, se actualizan los datos de la cita y se redirige a la lista de citas.
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