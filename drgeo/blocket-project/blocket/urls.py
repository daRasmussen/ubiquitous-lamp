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

from django.contrib import admin
from django.urls import path

from main import views as main_views
from account import views as account_views
from user_profile import views as user_profile_views
from conf.conf import Names

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_views.index, name=f"{Names.INDEX.value}"),
    path("register_user/", account_views.register_user, name=f"{Names.REGISTER_USER.value}"),
    path("login/", account_views.login_user, name=f"{Names.LOGIN_USER.value}"),
    path("logout/", account_views.logout_user, name=f"{Names.LOGOUT_USER.value}"),
    path("profile", user_profile_views.index, name=f"{Names.USER_PROFILE.value}")
]
