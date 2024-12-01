from cinemabiggu.models import Actor
from cinemabiggu.serializers import ActorSerializer
from rest_framework import viewsets


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all().order_by('id')

    def get_serializer_class(self):
        versions = {
            'v1': ActorSerializer
        }
        return versions[self.request.version or 'v1']
