from cinemabiggu.models import Room
from cinemabiggu.serializers import RoomSerializer
from cinemabiggu.permissions import IsViewer, IsEditor
from cinemabiggu.throttles import ViewerThrottle, EditorThrottle
from rest_framework import viewsets


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('room_id')
    permission_classes = [IsViewer | IsEditor]
    throttle_classes = [ViewerThrottle, EditorThrottle]

    def get_serializer_class(self):
        versions = {
            'v1': RoomSerializer
        }
        return versions[self.request.version or 'v1']
