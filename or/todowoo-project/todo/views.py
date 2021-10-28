from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

# Create your views here.
from todo.forms import TodoForm


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
    """"""
    return render(req, 'todo/currenttodos.html')


def logoutuser(req):
    if req.method == 'POST':
        logout(req)
        return redirect('home')


def home(req):
    return render(req, 'todo/home.html')


def loginuser(req):
    """ """
    if req.method == "GET":
        return render(req, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        """ Validate """
        user = authenticate(req, username=req.POST["username"], password=req.POST["password"])
        if user is None:
            return render(
                req,
                'todo/loginuser.html',
                {
                    'form': AuthenticationForm(), "error": "User and password did not match"
                }
            )
        else:
            login(req, user)
            return redirect('currenttodos')


def createtodo(req):
    if req.method == 'GET':
        return render(req, 'todo/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(req.POST)
            """ Don't put in the database yet. """
            new_todo = form.save(commit=False)
            new_todo.user = req.user
            """ Now we will save. """
            new_todo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(req, 'todo/createtodo.html', {'form': TodoForm(), "error": "Value Error" })
