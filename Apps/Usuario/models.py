from django.contrib.auth.hashers import check_password, make_password
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, nomusuario, correo, contra, celular, **extra_fields):
        user = self.model(
            nomusuario=nomusuario,
            correo=self.normalize_email(correo),
            celular=celular,
            **extra_fields
        )
        user.set_password(contra)
        user.save(using=self._db)
        return user

    def create_superuser(self, nomusuario, correo, contra=None, celular=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(nomusuario, correo, contra, celular, **extra_fields)

class Usuarios(AbstractBaseUser, PermissionsMixin):
    nomusuario = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50, unique=True)
    contra = models.CharField(max_length=200)
    celular = models.IntegerField(null=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nomusuario', 'celular']

    def __str__(self) -> str:
        return self.nomusuario

    def set_password(self, raw_password):
        self.contra = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.contra)

class Perfil(models.Model):
    provincia = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    total_publicaciones = models.IntegerField(default=0)
    usuario = models.OneToOneField(Usuarios, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.usuario.nomusuario

