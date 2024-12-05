from cinemabiggu.models import Room
from cinemabiggu.serializers import RoomSerializer
from rest_framework import viewsets


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('room_id')

    def get_serializer_class(self):
        versions = {
            'v1': RoomSerializer
        }
        return versions[self.request.version or 'v1']
