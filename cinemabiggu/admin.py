from django.contrib import admin
from cinemabiggu.models import Movie


class Movies(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'genre',
        'duration',
        'release_date',
        'avaliable',
    )
    list_display_links = ('id', 'title',)
    list_per_page = 20
    search_fields = ('title', 'genre', 'release_date', 'avaliable',)
    ordering = ('release_date',)


admin.site.register(Movie, Movies)
