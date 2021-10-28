from enum import Enum

from django.shortcuts import render


class Locations(str, Enum):
    INDEX = 'main/index.html'


def index(req):
    return render(req, Locations.INDEX)