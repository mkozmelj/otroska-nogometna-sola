from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from .forms import dodajanje
from obvestila.models import Obvestilo, Trener
from datetime import datetime

from django.contrib.auth.models import User

# Create your views here.
def index (request):
    if request.user.is_authenticated():
        user = request.user
        t1 = Trener.objects.get(uporabnisko_ime=user.get_username())
        url = t1.slika.url
        return render(request, 'obvestila/trener.html', {'user': user.get_username(), 'logged': user.is_authenticated(), 'url': url})
    else:
        return HttpResponseRedirect('/')

def odjava(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def dodaj(request):
    if request.user.is_authenticated():
        besedilo = request.POST['textarea']
        if besedilo!= "":
            user = request.user
            obvestilo = Obvestilo()
            obvestilo.besedilo = besedilo
            obvestilo.avtor = Trener.objects.get(uporabnisko_ime=user.get_username())
            obvestilo.datum = datetime.today()
            obvestilo.save()
            url = obvestilo.avtor.slika.url
            return render(request, 'obvestila/trener.html', {'user': user.get_username(), 'besedilo': 'Dodali ste besedilo', 'logged': user.is_authenticated(), 'url': url})
        else:
            return render(request, 'obvestila/trener.html',
                          {'bes': 'Vpisite besedilo'})

    else :
        return HttpResponseRedirect('/')

def zamenjajSliko(request):
    if request.user.is_authenticated:
        u = request.user
        t1 = Trener.objects.get(uporabnisko_ime=u.get_username())
        t1.slika = '/static/obvestila/img/' + str(request.POST['browse'])
        t1.save()
        return HttpResponseRedirect('/trener')
    else:
        return HttpResponseRedirect('/')