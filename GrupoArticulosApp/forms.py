from django import forms
from django.forms import ModelForm
from .models import Categoria

class IngresarCategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields=['descripcion']

