from django.contrib import messages
from django.contrib.auth import login
from django.db import IntegrityError
from django.shortcuts import render, redirect

from account.forms import SignUpForm
from account.models import Account
from conf.conf import Locations, Titles

from main.views import index


def register_user(req):
    context = {
        "title": Titles.REGISTER_USER.name
    }
    if req.method == 'GET':
        return render(req, Locations.REGISTER_USER, {
            "form": SignUpForm()
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