from django.urls import path, include

urlpatterns = [
    path('v1/', include('cinemabiggu.endpoints.v1.urls')),
]
