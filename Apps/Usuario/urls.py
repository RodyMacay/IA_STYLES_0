from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
path('', views.Login, name="login"),
path('registro/', views.Registro, name="registro"),
path('login/', LogoutView.as_view(template_name='Usuario/login.html'), name='logout'),
]