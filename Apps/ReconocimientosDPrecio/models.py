from django.db import models
from .utils import imgPrenda_media_path
from ..Usuario.models import Perfil
from djmoney.models.fields import MoneyField
# Create your models here.
class Imagenes (models.Model):
    ImagenDprenda=models.ImageField(upload_to=imgPrenda_media_path, null=True, blank=True)
    usuario =models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = None


    def __str__(self):
        return f'{self.ImagenDprenda}'
class DetalleIA(models.Model):
    marca = models.CharField(max_length=50)
    talla =models.IntegerField(null=True, default=None)
    precio = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    descripcion = models.CharField(max_length=150)
    condicion =models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    imagen = models.OneToOneField(Imagenes, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f' {self.descripcion}'
