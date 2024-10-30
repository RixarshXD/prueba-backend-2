from django import forms
from .models import Cita

class FormCitas(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'