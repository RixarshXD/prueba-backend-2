from django import forms
from ..citasMedicasApp.models import Pacientes


class FormPacientes(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'
