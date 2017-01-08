from django.shortcuts import render
from django.contrib.auth.models import User

def index (request):
    user = request.user
    return render(request, 'obvestila/urniki.html', {'logged': user.is_authenticated})

