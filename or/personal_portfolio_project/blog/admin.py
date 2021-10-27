from django.contrib import admin

# Register your models here.
from .models import Blog

""" I want to see this model inside the admin """
admin.site.register(Blog)