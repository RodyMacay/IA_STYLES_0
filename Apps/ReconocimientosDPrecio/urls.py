from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
path('vender/',login_required(views.Vender), name="vender"),

]