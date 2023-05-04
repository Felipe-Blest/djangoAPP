from django.forms import ModelForm
from .models import Persona

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ('rut', 'name', 'last_name')
