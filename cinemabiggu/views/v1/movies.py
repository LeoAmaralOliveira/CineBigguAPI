from cinemabiggu.models import Movie
from cinemabiggu.serializers import MovieSerializer
from rest_framework import viewsets


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
