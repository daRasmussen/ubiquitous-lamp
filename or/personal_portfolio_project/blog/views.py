from django.shortcuts import render


# Create your views here.
def all_blogs(req):
    return render(req, 'blog/all_blogs.html')
