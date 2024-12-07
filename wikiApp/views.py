from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import articuloWiki, temaWiki

def inicio(request):
    return render(request,'inicio.html')

def nuevoTema(request):
    if request.method == 'POST':
        nombreTema = request.POST.get('nombreTema')
        descripcionTema = request.POST.get('descripcionTema')
        temaWiki.objects.create(
            nombre = nombreTema,
            descripcion = descripcionTema
        )
        return HttpResponseRedirect(reverse('wikiApp:temas'))
    return render(request,'nuevoTema.html')

def temas(request):
    listaTemas = temaWiki.objects.all()
    return render(request,'temas.html',{
        'listaTemas': listaTemas
    }) 
    
def nuevoArticulo(request):
    if request.method == 'POST':
        tituloArticulo = request.POST.get('tituloArticulo')
        contenidoArticulo = request.POST.get('contenidoArticulo')
        temaArticulo = request.POST.get('temaArticulo')
        if temaArticulo != "0":
            objTema = temaWiki.objects.get(id = temaArticulo)
            articuloWiki.objects.create(
                titulo = tituloArticulo,
                contenido = contenidoArticulo,
                temaR = objTema
            )
        else:
            articuloWiki.objects.create(
                titulo = tituloArticulo,
                contenido = contenidoArticulo
            )
            
        return HttpResponseRedirect(reverse('wikiApp:articulos'))
    return render(request,'nuevoArticulo.html',{
        'listaTemas':temaWiki.objects.all()
    })

def articulos(request):
    listaArticulos = articuloWiki.objects.all()
    return render(request,'articulos.html',{
        'listaArticulos': listaArticulos
    }) 
