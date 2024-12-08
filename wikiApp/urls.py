from django.urls import path
from . import views

app_name='wikiApp'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('temas', views.temas, name='temas'),
    path('nuevoTema',views.nuevoTema,name='nuevoTema'), 
    path('verTema/<str:idTema>', views.verTema, name='verTema'),
    path('actualizarTema/<str:idTema>', views.actualizarTema, name='actualizarTema'),
    path('articulos', views.articulos, name='articulos'),  
    path('nuevoArticulo', views.nuevoArticulo, name='nuevoArticulo'), 
    path('verArticulo/<str:idArticulo>', views.verArticulo, name='verArticulo'),
    path('actualizarArticulo/<str:idArticulo>', views.actualizarArticulo, name='actualizarArticulo'),
    path('buscarArticulo', views.buscarArticulo, name='buscarArticulo'),
]