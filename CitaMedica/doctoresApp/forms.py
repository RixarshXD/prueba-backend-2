from django import forms
from .models import Doctor


class FormDoctor(forms.ModelForm):
    
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Nombre del doctor'}),
            
            'apellido': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Apellido del doctor'}),
            
            'rut': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Rut del doctor'}),
            
            'fechaNacimiento': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date',
                       'placeholder': 'Fecha de nacimiento'}),
            
            'especialidad': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Especialidad del doctor'}),
            
            'correo': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Correo del doctor'}),
        }
