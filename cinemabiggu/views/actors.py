from cinemabiggu.models import Actor
from cinemabiggu.serializers import ActorSerializer
from cinemabiggu.permissions import IsViewer, IsEditor
from cinemabiggu.throttles import ViewerThrottle, EditorThrottle
from rest_framework import viewsets


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all().order_by('id')
    permission_classes = [IsViewer | IsEditor]
    throttle_classes = [ViewerThrottle, EditorThrottle]

    def get_serializer_class(self):
        versions = {
            'v1': ActorSerializer
        }
        return versions[self.request.version or 'v1']
