from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario, Perfil


class Register_user(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña')

    class Meta:
        model = Usuario
        fields = ['username', 'correo', 'password1', 'password2', 'celular']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return password2


class Login_user(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
class UpdatePerfilform(forms.ModelForm):
    # Agrega campos adicionales para el usuario
    username = forms.CharField(max_length=150, required=True)
    celular = forms.IntegerField(required=False)  # Puedes ajustar esto según tus necesidades

    class Meta:
        model = Perfil
        fields = ['imagen', 'provincia', 'ciudad']

class UpdateUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'celular', 'correo']