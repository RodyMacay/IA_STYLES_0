from django import forms
from .models import Imagenes
from ..Usuario.models import Perfil


class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagenes
        fields = ['ImagenDprenda']

