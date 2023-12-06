
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Publicacion
from ..ReconocimientosDPrecio.models import Imagenes, DetalleIA
from ..Usuario.models import Perfil

from django.http import JsonResponse, Http404

def Inicio(request):
    datos = Publicacion.objects.all()
    for dato in datos:
        print(f"Nombre: {dato.DetalleIA.descripcion}, Precio: {dato.DetalleIA.precio}, Estado: {dato.DetalleIA.condicion}")
        if dato.DetalleIA.imagen.ImagenDprenda:
            print(f"Imagen: {dato.DetalleIA.imagen.ImagenDprenda.url}")
        else:
            print("No hay archivo asociado a esta publicación")
    categoria = DetalleIA.objects.values_list('tipo', flat=True).distinct()
    precios= DetalleIA.objects.values_list('precio', flat=True).distinct()
    estado= DetalleIA.objects.values_list('condicion', flat=True).distinct()
    print(categoria, precios)
    filtrar={
    'categoria': categoria,
    'precios': precios,
    'condicion': estado,
    }
    print(filtrar)
    return render(request, 'PublicacionDprendas/inicio.html', {
        'datos': datos,
        'filtrar': filtrar
    })



def Misproductos(request):
    try:
        perfil = Perfil.objects.get(usuario=request.user)
        productos = Publicacion.objects.filter(DetalleIA__imagen__usuario=perfil.usuario.id)
    except Perfil.DoesNotExist:
        raise Http404("El perfil del usuario no existe.")
    except Publicacion.DoesNotExist:
        productos = []  # No hay productos, establecer una lista vacía
    print('aqui los productos', productos)
    return render(request, 'PublicacionDprendas/MisProductos.html', {'productos': productos})
def Detalle(request,id_producto):
    producto = get_object_or_404(Publicacion, id=id_producto)
    # Construye la URL inversa usando reverse
    url = reverse('detalle', kwargs={'id_producto': producto.id})
    return render(request, 'PublicacionDprendas/Detalle.html',{
        'url': url,
        'producto': producto
    })



def buscar(request):
    categoria = request.GET.get('categoria')
    estado = request.GET.get('estado')

    # Aquí, estoy asumiendo que tienes un modelo llamado DetalleIA
    resultados = DetalleIA.objects.filter(tipo=categoria, condicion=estado)

    # Convertir los resultados a formato JSON
    resultados_json = [{'descripcion': item.descripcion,'precio':item.precio,'condicion': item.condicion, 'imagen_url': item.imagen.ImagenDprenda.url} for item in resultados]

    # Devolver los resultados de la búsqueda como JSON
    return JsonResponse({'resultados': resultados_json})
