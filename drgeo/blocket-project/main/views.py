from django.shortcuts import render

from conf.conf import Titles, Locations


def index(req):
    return render(req, Locations.INDEX, {"title": f"{Titles.INDEX}"})
