from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def Inicio (resquest):
   return render(resquest, 'PublicacionDprendas/inicio.html')


def Misproductos(resquest):
    return render(resquest, 'PublicacionDprendas/MisProductos.html')

def Detalle (request):
    return render(request, 'PublicacionDprendas/Detalle.html')