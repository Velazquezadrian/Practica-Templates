from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Gato


# Create your views here.

def gato(request):
    gatos = Gato.objects.order_by('id')
    template = loader.get_template('gato.html')
    title = 'Los gatos son cool'
    context = {
        'gatos': gatos,
        'title': title
    }
    return HttpResponse(template.render(context, request))
#ESTO FUE PARA SACAR DATOS DE LA BASE DE DATOS DE MODELS Y PASARLO A UNA TEMPLATES O HTML

def saludo(request):
    template = loader.get_template('saludo.html')
    big_title = 'Encabezado de la pagina'
    title = 'Aqui no hay gato'
    hola = {
        'big_title': big_title,
        'title': title
    }
    return HttpResponse(template.render(hola, request))