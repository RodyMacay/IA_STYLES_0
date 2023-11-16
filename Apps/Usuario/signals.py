from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Perfil
from .models import Usuario  # Asegúrate de importar tu modelo de usuario personalizado

@receiver(post_save, sender=Usuario)  # Usa tu modelo de usuario personalizado en lugar de get_user_model()
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)
