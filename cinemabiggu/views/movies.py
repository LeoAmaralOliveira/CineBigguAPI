from cinemabiggu.models import Movie
from cinemabiggu.serializers import MovieSerializer
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('id')
    filter_backends = [OrderingFilter]
    ordering_fields = ['release_date']

    def get_serializer_class(self):
        versions = {
            'v1': MovieSerializer
        }
        return versions[self.request.version or 'v1']
