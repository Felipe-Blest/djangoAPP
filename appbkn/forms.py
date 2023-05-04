from django.forms import ModelForm
from .models import persona

class PersonaForm(ModelForm):
    class Meta:
        model = persona
        fields = ('rut', 'name', 'last_name')
