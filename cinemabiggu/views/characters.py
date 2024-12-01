from cinemabiggu.models import Character
from cinemabiggu.serializers import CharacterSerializer
from rest_framework import viewsets


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().order_by('id')

    def get_serializer_class(self):
        versions = {
            'v1': CharacterSerializer
        }
        return versions[self.request.version or 'v1']
