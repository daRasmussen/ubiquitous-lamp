from django.shortcuts import render

from conf.conf import Locations, Titles


def register_user(req):
    return render(req, Locations.REGISTER_USER, {"title": Titles.REGISTER_USER.name})