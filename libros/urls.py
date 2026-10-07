from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('inicio/', views.inicio, name='inicio'),
    path('agregar/', views.agregar_libro, name='agregar_libro'),
    path('salir/', views.salir, name='salir'),
]