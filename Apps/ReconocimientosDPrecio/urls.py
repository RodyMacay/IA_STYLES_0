from django.urls import path
from . import views

urlpatterns = [
path('vender/', views.Vender, name="vender"),

]