from django.urls import path, include
from cinemabiggu.api.versions.v1 import urls as v1_urls


urlpatterns = [
    path('v1/', include(v1_urls))
]
