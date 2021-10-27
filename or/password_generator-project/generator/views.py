import random

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(req):
    return render(req, 'generator/home.html', {"password": "123456"})


def about(req):
    return render(req, 'generator/about.html')


def password(req):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if req.GET.get('uppercase'):
        characters.extend([x.upper() for x in characters])
    if req.GET.get('special'):
        characters.extend('!"#¤%&/()=?')
    if req.GET.get('numbers'):
        characters.extend("12345678790")
    length = int(req.GET.get('length', 12))
    passwd = ""
    for x in range(length):
        passwd += random.choice(characters)

    return render(req, 'generator/password.html', {"password": passwd})
