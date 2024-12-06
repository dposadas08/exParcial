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
