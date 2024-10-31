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
                           'placeholder': 'Fecha de la cita'}),
        }