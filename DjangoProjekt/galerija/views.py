from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

def index (request):
    user = request.user
    print(user)
    return render(request, 'obvestila/galerija.html', {'logged': user.is_authenticated()})

def odjava(request):
    logout(request)
    return HttpResponseRedirect('/')

