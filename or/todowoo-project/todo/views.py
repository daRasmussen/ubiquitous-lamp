from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.utils import timezone

from todo.forms import TodoForm
from todo.models import Todo


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


# noinspection PyUnresolvedReferences
def currenttodos(req):
    """"""
    """ isnull_ datecompleted, only show uncompleted tasks in current. """
    todos = Todo.objects.filter(user=req.user, datecompleted__isnull=True)
    return render(req, 'todo/currenttodos.html', {"todos": todos})


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
            return render(req, 'todo/createtodo.html', {'form': TodoForm(), "error": "Value Error"})


def viewtodo(req, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=req.user)
    if req.method == "GET":
        form = TodoForm(instance=todo)
        return render(req, 'todo/viewtodo.html', {"todo": todo, "form": form})
    else:
        try:
            form = TodoForm(req.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(
                req, 'todo/viewtodo.html', {
                    "todo": todo,
                    "form": form,
                    "error": "Bad info!"})


def completetodo(req, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=req.user)
    if req.method == "POST":
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currenttodos')


def deletetodo(req, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=req.user)
    if req.method == "POST":
        todo.delete()
        return redirect('currenttodos')
