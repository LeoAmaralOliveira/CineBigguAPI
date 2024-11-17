from rest_framework import generics
from cinemabiggu.models import Actor
from cinemabiggu.serializers.v1.actors import ActorSerializer
from rest_framework import status
from rest_framework.response import Response


class ActorListCreateView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class AllActorsListView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    partial = True


class ActorDeleteView(generics.DestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            data={"message": "Actor deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
