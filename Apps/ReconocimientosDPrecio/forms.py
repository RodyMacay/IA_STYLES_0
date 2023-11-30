
from django import forms
from .models import DetalleIA

class DetalleIAForm(forms.ModelForm):
    class Meta:
        model = DetalleIA
        fields = ['descripcion','tipo','talla','marca','condicion', 'precio']
