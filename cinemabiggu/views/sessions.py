from cinemabiggu.models import Session
from cinemabiggu.serializers.sessions import SessionSerializer
from cinemabiggu.permissions import IsViewer, IsEditor
from cinemabiggu.throttles import ViewerThrottle, EditorThrottle
from rest_framework import viewsets


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all().order_by('id')
    permission_classes = [IsViewer | IsEditor]
    throttle_classes = [ViewerThrottle, EditorThrottle]

    def get_serializer_class(self):
        versions = {
            'v1': SessionSerializer
        }
        return versions[self.request.version or 'v1']
