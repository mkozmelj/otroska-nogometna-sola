from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect
from .models import Obvestilo
from django.contrib.auth.models import User
from datetime import date

def index (request):
    vsa_obvestila = Obvestilo.objects.all()
    user = request.user
    return render(request, 'obvestila/obvestila.html', { 'vsa_obvestila': vsa_obvestila, 'logged': user.is_authenticated()})

def detail (request, obvestila_id):
    try:
        obvestilo = Obvestilo.objects.get(pk=obvestila_id)
    except Obvestilo.DoesNotExist:
        raise Http404("Obvestilo ne obstaja!" + str(obvestila_id))
    return render(request, 'obvestila/podrobnosti.html', {'besedilo': obvestilo})

def posodobi(request, obvestila_id):
    bes = request.POST['textarea']
    try:
        obvestilo = Obvestilo.objects.get(pk=obvestila_id)
        obvestilo.besedilo = bes
        obvestilo.datum = date.today()
        obvestilo.save()
    except Obvestilo.DoesNotExist:
        raise Http404("Obvestilo ne obstaja!" + str(obvestila_id))
    return HttpResponseRedirect('/obvestila')

def izbrisi(request, obvestila_id):
    try:
        obvestilo = Obvestilo.objects.get(pk=obvestila_id)
        obvestilo.delete()
    except Obvestilo.DoesNotExist:
        raise Http404("Obvestilo ne obstaja!" + str(obvestila_id))
    return HttpResponseRedirect('/obvestila')
