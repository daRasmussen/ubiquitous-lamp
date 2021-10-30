from enum import Enum

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from conf.conf import Titles, Locations


def index(req):
    return render(req, Locations.INDEX, {"title": f"{Titles.INDEX}"})


def register_user(req):
    context = {
        "title": f"{Titles.REGISTER_USER}",
    }
    if req.method == "GET" and req.user is None:
        return render(req, Locations.REGISTER_USER, dict(
            {
                "form": CustomUserCreationForm()
            }, **context))
    elif req.method == "POST" and req.user is None:
        if req.POST["password1"] == req.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=req.POST["username"],
                    email=req.POST["email"],
                    password=req.POST["password1"],
                )
                user.save()
                messages.success(req, f"✨ ✨ ✨ Welcome {user.username} to Blocket! ✨ ✨ ✨")
                login(req, user)
                messages.success(req, f"👏 👏 👏 {user.username} has successfully logged in! 👏 👏 👏")
                return redirect('index')
            except IntegrityError:
                messages.error(req, "🤔 🤔 🤔 Something went wrong. 🤔 🤔 🤔")
        else:
            messages.warning(req, "Ops! Your passwords did not match! ")
            return render(req, Locations.REGISTER_USER, context)
    elif req.method == "GET" and req.user:
        return redirect("profile")


