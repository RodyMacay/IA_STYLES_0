from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def Inicio (resquest):
   return render(resquest, 'inicio.html')


def Misproductos(resquest):
    return render(resquest, 'MisProductos.html')