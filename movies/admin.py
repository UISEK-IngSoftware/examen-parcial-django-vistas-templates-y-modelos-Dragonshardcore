from django.apps import AppConfig
from .models import Movie
from django.contrib import admin

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass

