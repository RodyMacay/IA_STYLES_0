from django.contrib.auth.hashers import check_password, make_password
from django.db import models

# Create your models here.
class Usuarios (models.Model):
    nomusuario = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    contra = models.CharField(max_length=200)
    celular = models.IntegerField(null=False)

    def __str__(self) -> str:
        return self.nomusuario

    def set_password(self, raw_password):
        # Almacena la contraseña de manera segura utilizando make_password
        self.contra = make_password(raw_password)

    def check_password(self, raw_password):
        # Verifica la contraseña utilizando check_password
        return check_password(raw_password, self.contra)
class Perfil(models.Model):
    provincia = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    total_publicaciones = models.IntegerField(default=0)
    usuario = models.OneToOneField(Usuarios, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.usuario.nomusuario

