from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
path('inicio/', login_required(views.Inicio), name="inicio"),
path('misproductos/', login_required(views.Misproductos), name="MisProductos"),
path('detalle/<int:id_producto>/', login_required(views.Detalle), name="detalle"),
path('buscar/', login_required(views.buscar), name="buscar"),
]