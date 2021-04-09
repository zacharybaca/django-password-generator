from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def index(request):
    return render(request, 'index.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 8))

    created_password = ''
    for x in range(length):
        created_password += random.choice(characters)
    return render(request, 'password.html', {'password': created_password})

def about(request):
    return render(request, 'about.html')