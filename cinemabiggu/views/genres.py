from cinemabiggu.models import Genre
from cinemabiggu.serializers import GenreSerializer
from rest_framework import viewsets


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('id')

    def get_serializer_class(self):
        versions = {
            'v1': GenreSerializer
        }
        return versions[self.request.version or 'v1']
