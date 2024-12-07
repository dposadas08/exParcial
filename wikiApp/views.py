from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import articuloWiki, temaWiki

def inicio(request):
    return render(request,'inicio.html')

# --- Tema ---
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
    
def actualizarTema(request, idTema):   
    objTema = temaWiki.objects.get(id = idTema)
    if request.method == 'POST':
        nombreTema = request.POST.get('nombreTema')
        descripcionTema = request.POST.get('descripcionTema')
        objTema.nombre = nombreTema
        objTema.descripcion = descripcionTema
        objTema.save()
        return HttpResponseRedirect(reverse('wikiApp:temas'))
    return render(request,'actualizarTema.html',{
        'tema': objTema
    })

# --- Articulo ---  
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
    
def actualizarArticulo(request, idArticulo):   
    objArticulo = articuloWiki.objects.get(id = idArticulo)
    if request.method == 'POST':
        tituloArticulo = request.POST.get('tituloArticulo')
        contenidoArticulo = request.POST.get('contenidoArticulo')
        temaArticulo = request.POST.get('temaArticulo') 
        objArticulo.titulo = tituloArticulo
        objArticulo.contenido = contenidoArticulo
        if temaArticulo != "0":
            objTema = temaWiki.objects.get(id = temaArticulo)
            objArticulo.temaR = objTema
        else:
            objArticulo.temaR = None
        objArticulo.save()
        return HttpResponseRedirect(reverse('wikiApp:articulos'))
    return render(request,'actualizarArticulo.html',{
        'articulo': objArticulo,
        'listaTemas':temaWiki.objects.all()
    })

def articulos(request):
    listaArticulos = articuloWiki.objects.all()
    return render(request,'articulos.html',{
        'listaArticulos': listaArticulos
    }) 
