from cinemabiggu.models import Actor
from cinemabiggu.serializers import ActorSerializer
from rest_framework import viewsets


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
