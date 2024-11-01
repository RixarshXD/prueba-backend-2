from django import forms
from .models import Pacientes


class FormPacientes(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Nombre del paciente'}),
            
            'apellido': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Apellido del paciente'}),
            
            'rut': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Rut del paciente'}),
            
            'fechaNacimiento': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date',
                       'placeholder': 'Fecha de nacimiento'}),
            
            'correo': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Correo del paciente'}),
        }


    def clean_especialidad(self):
        especialidad = self.cleaned_data.get('especialidad')
        if especialidad == 'Sin especialidad':
            raise forms.ValidationError("Por favor, selecciona una especialidad.")
        return especialidad
    
    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if "-" not in rut:
            raise forms.ValidationError("El RUT debe contener el guión.")
        if "." in rut:
            raise forms.ValidationError("Ingrese su RUT sin puntos.")

        numerico, codigo_verificador = rut.split("-")

        if len(numerico) < 7 or len(numerico) > 8:
            raise forms.ValidationError("La longitud de la parte numérica no es válida.")
        if not numerico.isdigit():
            raise forms.ValidationError("La parte numérica debe ser un número.")
        if len(codigo_verificador) != 1 or (not codigo_verificador.isdigit() and codigo_verificador.lower() != "k"):
            raise forms.ValidationError("El código verificador debe ser un número o 'K'.")
        return rut
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre.isalpha():
            raise forms.ValidationError("Un nombre solo debe contener letras.")
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if not apellido.isalpha():
            raise forms.ValidationError("Un apellido solo debe contener letras.")
        return apellido
