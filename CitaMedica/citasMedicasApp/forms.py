from django import forms
from .models import Cita

class FormCitas(forms.ModelForm):
    
    
    class Meta:
        model = Cita
        fields = '__all__'
        widgets = {
              'horaCita': forms.TimeInput(
                     attrs={'class': 'form-control',
                            'type': 'time',
                            'placeholder': 'Hora de la cita'}),
            
              'fechaCita': forms.DateInput(
                     attrs={'class': 'form-control',
                           'type': 'date',
                           'initial': '31-12-2024'}),
            
              'diagnostico': forms.TextInput(
                     attrs={'class': 'form-control',
                           'placeholder': 'Diagnostico'}),
            
              'motivo': forms.TextInput(
                     attrs={'class': 'form-control',
                           'placeholder': 'Motivo de la cita'}),
            
              'observacion': forms.TextInput(
                     attrs={'class': 'form-control',
                           'placeholder': 'Observaciones'}),
              'doctor': forms.Select(
                     attrs={'class': 'form-control'}),
              'paciente': forms.Select(
                     attrs={'class': 'form-control'}),
        }