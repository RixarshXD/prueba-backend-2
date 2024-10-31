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
            
            'rut': forms.NumberInput(
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

