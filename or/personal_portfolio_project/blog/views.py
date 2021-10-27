from django.shortcuts import render
from .models import Blog


# Create your views here.
# noinspection PyUnresolvedReferences
def all_blogs(req):
    posts = Blog.objects.order_by('-date')[:1]
    return render(req, 'blog/all_blogs.html', {'posts': posts})
