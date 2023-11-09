from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuarios
from django.contrib.auth.forms import AuthenticationForm


class Register_user (forms.ModelForm):
    class Meta:
        model = Usuarios
        # al usar __all__ crear un form con todos los campos de mi modelo
        fields = '__all__'

class Login_user(AuthenticationForm):
    class Meta:
        model = Usuarios
        fields = ['nomusuario', 'contra']

