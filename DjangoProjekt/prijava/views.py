from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .forms import vpis, email
from obvestila.models import Stars
from django.shortcuts import render

def poskus_prijave(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    form = vpis(request.POST)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect('/trener/')
    else:
        # Return an 'invalid login' error message.
        return render(request, 'obvestila/prijava.html', {'form': form, 'er': 'Vnesite pravilno uporabniško ime in geslo'})

from django.shortcuts import render


def index (request):
    form = vpis(request.POST)
    formular = email(request.POST)
    return render(request, 'obvestila/prijava.html', {'form': form, 'formular': formular})


def regist(request):
    form = vpis(request.POST)
    formular = email(request.POST)
    if Stars.objects.filter(email=formular).exists():
        return render(request, 'obvestila/prijava.html',
                      {'form': form, 'formular': formular, 'errr': 'Ta mail že obstaja v bazi.'})
    else:
        ob = Stars()
        ob.email = request.POST['mail']
        ob.save()
        return render(request, 'obvestila/prijava.html', {'form': form, 'formular': formular, 'err': 'Dodani ste v bazo podatkov.'})