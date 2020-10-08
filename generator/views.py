from django.shortcuts import render

from django.http import HttpResponse


import random

# Create your views here.

def home(request):
    print('Hello')
    return render(request, 'generator/index.html', {'password':'hi1233qerw33214qeee'})

def about(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    characters.extend(list('0123456789'))
    characters.extend(list('!@#$%^&*()_'))

    password = ''
    for pswd in range(20):
        password += random.choice(characters)

    return render(request, 'generator/about.html', {'password': password})

def password(request):
    characters =  list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    # length = 10
    length = int(request.GET.get('length', 12))
    password = ''
    for x in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password})
