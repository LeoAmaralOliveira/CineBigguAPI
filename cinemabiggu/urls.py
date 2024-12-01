from django.urls import path, include
from cinemabiggu.views import (
    MovieViewSet, ActorViewSet,
    CharacterViewSet, GenreViewSet
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet, basename='Movies')
router.register(r'actors', ActorViewSet, basename='Actors')
router.register(r'characters', CharacterViewSet, basename='Characters')
router.register(r'genres', GenreViewSet, basename='Genres')


urlpatterns = [
    path('', include(router.urls)),
]
