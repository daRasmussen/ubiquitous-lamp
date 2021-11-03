from django.shortcuts import render

from conf.conf import Locations, Titles


def index(req):
    context = {
        "title": Titles.USER_PROFILE.value
    }
    return render(req, Locations.USER_PROFILE.value, context)
