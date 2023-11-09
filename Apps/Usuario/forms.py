from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuarios
from django.contrib.auth.forms import AuthenticationForm


# En tu forms.py
from django import forms
from .models import Usuarios

class Register_user(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nomusuario', 'correo', 'contra', 'celular']

class Login_user(AuthenticationForm):
    class Meta:
        model = Usuarios
        fields = ['nomusuario', 'contra']

