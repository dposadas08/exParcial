from django.urls import path
from . import views

app_name='wikiApp'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevoTema',views.nuevoTema,name='nuevoTema'),
    path('temas', views.temas, name='temas'),
    path('nuevoArticulo', views.nuevoArticulo, name='nuevoArticulo'), 
    path('articulos', views.articulos, name='articulos') 
]