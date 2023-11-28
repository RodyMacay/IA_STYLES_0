from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
urlpatterns = [
path('', views.Login, name="login"),
path('registro/', views.Registro, name="registro"),
path('login/', LogoutView.as_view(template_name='Usuario/login.html'), name='logout'),
path ('perfil/', login_required(views.Perfil), name='perfil')
]