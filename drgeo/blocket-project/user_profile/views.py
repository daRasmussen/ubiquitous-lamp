from django.shortcuts import render

from conf.conf import Locations, Titles
from user_profile.forms import ProfileForm


def index(req):
    context = {
        "title": Titles.USER_PROFILE.value,
        "form": ProfileForm()
    }
    return render(req, Locations.USER_PROFILE.value, context)
