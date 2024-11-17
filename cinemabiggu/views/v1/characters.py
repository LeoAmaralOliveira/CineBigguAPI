from rest_framework import generics
from cinemabiggu.models import Character
from cinemabiggu.serializers.v1.characters import CharacterSerializer
from rest_framework import status
from rest_framework.response import Response


class CharacterListCreateView(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class AllCharactersListView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    partial = True


class CharacterDeleteView(generics.DestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            data={"message": "Character deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
