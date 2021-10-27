from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect


# Create your views here.
def signupuser(req):
    """"""
    if req.method == "GET":
        return render(req, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        """ Validate password """
        if req.POST['password1'] == req.POST['password2']:
            """ Create a new user """
            try:
                """ Check if user does not exists. """
                user = User.objects.create_user(req.POST["username"], password=req.POST["password1"])
                user.save()
                login(req, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(req, 'todo/signupuser.html', {
                    "form": UserCreationForm(), "error": "User already in exists!"}
                              )
        else:
            """ Tell the user the passwords didn't match! """
            return render(req, 'todo/signupuser.html', {
                "form": UserCreationForm(), "error": "Password didn't not match!"}
            )


def currenttodos(req):
    return render(req, 'todo/currenttodos.html')