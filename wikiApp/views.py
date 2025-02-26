from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import articuloWiki, temaWiki

def inicio(request):
    return render(request,'inicio.html',{
        'listaTemas':temaWiki.objects.all()
    }) 

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
    return render(request,'nuevoTema.html',{
        'listaTemas':temaWiki.objects.all()
    })

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
        'tema': objTema,
        'listaTemas':temaWiki.objects.all()
    })
    
def verTema(request, idTema):
    objTema = temaWiki.objects.get(id = idTema)
    listaArticulos = objTema.articulowiki_set.all()
    return render(request,'verTema.html',{
        'tema':objTema,
        'listaArticulos':listaArticulos,
        'listaTemas':temaWiki.objects.all(),
    })
    
# --- Articulo ---  
def nuevoArticulo(request):
    if request.method == 'POST':
        tituloArticulo = request.POST.get('tituloArticulo')
        contenidoArticulo = request.POST.get('contenidoArticulo')
        temaArticulo = request.POST.get('temaArticulo')
        if temaArticulo != "":
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
        if temaArticulo != "":
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
        'listaArticulos': listaArticulos,
        'listaTemas':temaWiki.objects.all()
    }) 
    
def verArticulo(request, idArticulo):
    objArticulo = articuloWiki.objects.get(id = idArticulo) 
    return render(request,'verArticulo.html',{
        'articulo': objArticulo,
        'listaTemas':temaWiki.objects.all()
    })

def buscarArticulo(request):
    texto = request.POST.get('texto')
    listaArticulos = articuloWiki.objects.filter(titulo__contains = texto)
    return render(request,'buscarArticulo.html',{
        'listaArticulos': listaArticulos,
        'listaTemas':temaWiki.objects.all()
    })