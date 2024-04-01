from django.contrib import admin
from .models import Movie, Actor, Genre

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

