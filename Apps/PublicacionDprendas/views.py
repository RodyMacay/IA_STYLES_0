
from django.shortcuts import render
from .models import Publicacion
from ..Usuario.models import Perfil


def Inicio(request):
    datos = Publicacion.objects.all()
    for dato in datos:
        print(f"Nombre: {dato.DetalleIA.descripcion}, Precio: {dato.DetalleIA.precio}, Estado: {dato.DetalleIA.condicion}")
        if dato.DetalleIA.imagen.ImagenDprenda:
            print(f"Imagen: {dato.DetalleIA.imagen.ImagenDprenda.url}")
        else:
            print("No hay archivo asociado a esta publicación")

    return render(request, 'PublicacionDprendas/inicio.html', {'datos': datos})



def Misproductos(resquest):
    perfil = Perfil.objects.get(usuario=resquest.user)
    print(perfil.usuario)
    productos = Publicacion.objects.filter(DetalleIA__imagen__usuario=perfil.usuario.id)
    print(productos)
    return render(resquest, 'PublicacionDprendas/MisProductos.html',
                  {'productos': productos})
def Detalle(request):
    return render(request, 'PublicacionDprendas/Detalle.html')