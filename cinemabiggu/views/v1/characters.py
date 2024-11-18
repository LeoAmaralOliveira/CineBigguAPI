from cinemabiggu.models import Character
from cinemabiggu.serializers import CharacterSerializer
from rest_framework import viewsets


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
