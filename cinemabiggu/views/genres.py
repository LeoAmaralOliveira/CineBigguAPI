from cinemabiggu.models import Genre
from cinemabiggu.serializers import GenreSerializer
from cinemabiggu.permissions import IsViewer, IsEditor
from cinemabiggu.throttles import ViewerThrottle, EditorThrottle
from rest_framework import viewsets


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('id')
    permission_classes = [IsViewer | IsEditor]
    throttle_classes = [ViewerThrottle, EditorThrottle]

    def get_serializer_class(self):
        versions = {
            'v1': GenreSerializer
        }
        return versions[self.request.version or 'v1']
