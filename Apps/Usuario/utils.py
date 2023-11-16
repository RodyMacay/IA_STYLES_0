
def user_media_path(instance, filename):
    # La función generará rutas del tipo: "usuarios/imagenes_perfil/username/filename"
    return f'Usuario/imagenes_perfil/{instance.usuario.username}/{filename}'