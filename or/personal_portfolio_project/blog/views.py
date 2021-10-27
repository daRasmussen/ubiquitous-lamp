from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
# noinspection PyUnresolvedReferences
def all_blogs(req):
    posts = Blog.objects.order_by('-date')[:1]
    return render(req, 'blog/all_blogs.html', {'posts': posts})


def detail(req, blog_id):
    post = get_object_or_404(Blog,pk=blog_id)
    return render(req, 'blog/detail.html', {'post': post})