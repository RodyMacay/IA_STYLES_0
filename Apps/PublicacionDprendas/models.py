from django.db import models
from ..ReconocimientosDPrecio.models import DetalleIA
# Create your models here.
class Publicacion (models.Model):
    fecha_publicacion = models.DateTimeField(auto_now=True)
    DetalleIA = models.OneToOneField(DetalleIA, on_delete=models.CASCADE, null=False)

