from enum import Enum

from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm


class Names(str, Enum):
    APP = 'Blocket'
    REGISTER_USER = 'Sign up'


class Locations(str, Enum):
    INDEX = 'main/index.html',
    REGISTER_USER = 'main/register_user.html'


def index(req):
    return render(req, Locations.INDEX, {"title": f"{Names.APP}"})


def register_user(req):
    if req.method == "POST":
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, 'Account created successfully!')
    else:
        form = CustomUserCreationForm()
    return render(req, Locations.REGISTER_USER, {"title": f"{Names.REGISTER_USER}", "form": form})
