from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View

from account.forms import SignUpForm, LoginForm
from account.models import Account
from conf.conf import Locations, Titles, Names

from main.views import index


def register_user(req):
    context = {
        "title": Titles.REGISTER_USER.value
    }
    if req.method == 'GET':
        return render(req, Locations.REGISTER_USER, {
            **{
                "form": SignUpForm()
            },
            **context
        })
    elif req.method == 'POST':
        try:
            user = Account.objects.create_user(
                username=req.POST["username"],
                email=req.POST["email"],
                password=req.POST["password"]
            )
            user.save()
            messages.success(req, f"✨ ✨ ✨ Welcome {user.username} to Blocket! ✨ ✨ ✨")
            login(req, user)
            messages.success(req, f"👏 👏 👏 {user.username} has successfully logged in! 👏 👏 👏")
        except IntegrityError:
            messages.error(req, "🤔 🤔 🤔 Username taken. 🤔 🤔 🤔")
        return redirect(index)


def login_user(req):
    context = {
        "title": Titles.LOGIN_USER.name
    }
    if req.method == 'GET':
        return render(req, Locations.LOGIN_USER.value, {
            **{
                "form": LoginForm()
            },
            **context
        })
    elif req.method == 'POST':
        user = authenticate(req, username=req.POST["email"], password=req.POST["password"])
        if user is None:
            messages.error(req, f"🤔 🤔 🤔 Ops! Username and password does not match. 🤔 🤔 🤔")
            return render(req, Locations.LOGIN_USER.value, {
                **context,
                **{
                    "form": LoginForm()
                }
            })
        else:
            login(req, user)
            messages.success(req, f"👏 👏 👏 Welcome back! 👏 👏 👏")
            return redirect(Names.INDEX.value)


def logout_user(req):
    if req.method == 'POST':
        logout(req)
        messages.success(req, f"👏 👏 👏 Good bye! 👏 👏 👏")
        return redirect(Names.INDEX.value)