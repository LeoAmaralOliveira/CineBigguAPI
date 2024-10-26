from django.contrib import admin
from django.urls import path, include
from cinemabiggu.views import (
    MovieViewSet
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('movies', MovieViewSet, basename='Movies')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
