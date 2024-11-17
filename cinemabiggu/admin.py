from django.contrib import admin
from cinemabiggu.models import Movie, Actor, Character


class Movies(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'genre',
        'duration',
        'release_date',
        'avaliable',
        'created_at',
        'updated_at',
    )
    list_display_links = ('id', 'title',)
    list_per_page = 20
    search_fields = ('title', 'genre', 'release_date', 'avaliable',)
    ordering = ('release_date',)


class Actors(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'birth_date',
        'awards',
        'created_at',
        'updated_at',
    )
    list_display_links = ('id', 'name',)
    list_per_page = 20
    search_fields = ('name',)
    ordering = ('created_at',)


class Characters(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'movie',
        'actor',
        'created_at',
        'updated_at',
    )
    list_display_links = ('id', 'name',)
    list_per_page = 20
    search_fields = ('name',)
    ordering = ('created_at',)


admin.site.register(Movie, Movies)
admin.site.register(Actor, Actors)
admin.site.register(Character, Characters)
