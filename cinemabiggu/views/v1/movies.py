from rest_framework import generics
from cinemabiggu.models import Movie
from cinemabiggu.serializers.v1.movies import MovieSerializer
from rest_framework import status
from rest_framework.response import Response


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class AllMoviesListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    partial = True


class MovieDeleteView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            data={"message": "Movie deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
