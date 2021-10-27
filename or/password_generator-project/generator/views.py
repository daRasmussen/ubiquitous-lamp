from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(req):
    return HttpResponse("Hello World/")


def eggs(req):
    return HttpResponse("Eggs är great! ")
