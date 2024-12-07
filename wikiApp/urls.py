from django.urls import path
from . import views

app_name='wikiApp'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('temas', views.temas, name='temas'),
    path('nuevoTema',views.nuevoTema,name='nuevoTema'),
    path('actualizarTema/<str:idTema>', views.actualizarTema, name='actualizarTema'),
    path('articulos', views.articulos, name='articulos'),  
    path('nuevoArticulo', views.nuevoArticulo, name='nuevoArticulo'), 
    path('actualizarArticulo/<str:idArticulo>', views.actualizarArticulo, name='actualizarArticulo'),
]