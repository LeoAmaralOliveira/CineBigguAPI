from cinemabiggu.models import Movie
from cinemabiggu.serializers import MovieSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['release_date']
    search_fields = ['title', 'genre']

    def get_serializer_class(self):
        return MovieSerializer
