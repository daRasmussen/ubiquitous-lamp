from django.urls import path, include

""" importing the blog/views.py """
from . import views

urlpatterns = [
    path('', views.all_blogs, name="all_blogs"),
]
