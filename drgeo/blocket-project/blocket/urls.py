"""blocket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from enum import Enum

from django.contrib import admin
from django.urls import path

from main import views as main_views
from account import views as account_views
from conf.conf import Names

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_views.index, name=f"{Names.INDEX}"),
    path("register_user/", account_views.register_user, name=f"{Names.REGISTER_USER}"),
]
