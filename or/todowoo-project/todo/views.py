from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def signupuser(req):
    """"""
    if req.method == "GET":
        return render(req, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        """ Validate password """
        if req.POST['password1'] == req.POST['password2']:
            """ Create a new user """
            user = User.objects.create_user(req.POST["username"], password=req.POST["password1"])
            user.save()
        else:
            print("Hello")
            """ TODO: Tell the user the passwords didn't match! """
