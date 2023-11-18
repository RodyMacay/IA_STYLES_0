from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import user_media_path

class Usuario(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    correo = models.EmailField(max_length=50, unique=True)
    celular = models.IntegerField(null=True, default=None)

    OPCIONES_ROL = [
        ('usuario', 'Usuario normal'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')

class Perfil(models.Model):
    imagen = models.ImageField(upload_to=user_media_path, null=True, blank=True)
    provincia = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    total_publicaciones = models.IntegerField(default=0)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.usuario.username
