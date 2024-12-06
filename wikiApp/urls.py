from django.urls import path
from . import views

app_name='wikiApp'


urlpatterns = [
    path('', views.inicio, name='inicio')
    
]