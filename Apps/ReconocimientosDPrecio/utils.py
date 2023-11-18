from Apps.Usuario.models import Usuario


def imgPrenda_media_path(instance, filename):
    # Verifica si el usuario está definido antes de acceder a sus atributos
    if instance.usuario:
        return f'ReconocimientosDPrecio/imagenesPrendas/{instance.usuario.usuario}/{filename}'
    else:
        # Si el usuario no está definido, puedes manejarlo de alguna manera (por ejemplo, usando un valor predeterminado)
        return f'ReconocimientosDPrecio/imagenesPrendas/default/{filename}'
