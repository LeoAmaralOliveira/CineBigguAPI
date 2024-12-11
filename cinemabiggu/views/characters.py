from cinemabiggu.models import Character
from cinemabiggu.serializers import CharacterSerializer
from cinemabiggu.permissions import IsViewer, IsEditor
from cinemabiggu.throttles import ViewerThrottle, EditorThrottle
from rest_framework import viewsets


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().order_by('id')
    permission_classes = [IsViewer | IsEditor]
    throttle_classes = [ViewerThrottle, EditorThrottle]

    def get_serializer_class(self):
        versions = {
            'v1': CharacterSerializer
        }
        return versions[self.request.version or 'v1']
