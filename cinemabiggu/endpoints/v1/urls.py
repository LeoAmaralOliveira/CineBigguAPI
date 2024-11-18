from django.urls import path, include
from cinemabiggu.views import (
    MovieViewSet, ActorViewSet, CharacterViewSet
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'characters', CharacterViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
