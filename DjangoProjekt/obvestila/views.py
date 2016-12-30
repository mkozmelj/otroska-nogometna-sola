from django.shortcuts import render
from django.http import Http404
from django.http import  HttpResponse
from .models import Obvestila

def index (request):
    vsa_obvestila = Obvestila.objects.all()
    return render(request, 'obvestila/obvestila.html', { 'vsa_obvestila': vsa_obvestila})

def detail (request, obvestila_id):
    try:
        obvestilo = Obvestila.objects.get(pk=obvestila_id)
    except Obvestila.DoesNotExist:
        raise Http404("Obvestilo ne obstaja!" + str(obvestila_id))
    return render(request, 'obvestila/podrobnosti.html', { 'obvestilo': obvestilo})