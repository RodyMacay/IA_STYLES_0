from Apps.Usuario.models import Usuario


def imgPrenda_media_path(instance, filename):
    # La función generará rutas del tipo: "usuarios/imagenes_perfil/username/filename"
    return f'ReconocimientosDPrecio/imagenes,_prendas/{instance.usuario.usuario}/{filename}'