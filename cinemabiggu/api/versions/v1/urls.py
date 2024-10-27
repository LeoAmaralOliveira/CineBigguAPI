from django.urls import path
from cinemabiggu.api.versions.v1.views import movie_list, movie_details


urlpatterns = [
    path('movies', movie_list, name='movies'),
    path('movies/<int:id>', movie_details, name='movie_details'),
]
