from django.urls import path
from cinemabiggu.views.v1.movies import (
    MovieListCreateView,
    MovieDetailView,
    AllMoviesListView,
    MovieDeleteView,
    MovieUpdateView
)
from cinemabiggu.views.v1.actors import (
    ActorListCreateView,
    ActorDetailView,
    AllActorsListView,
    ActorDeleteView,
    ActorUpdateView
)
from cinemabiggu.views.v1.characters import (
    CharacterListCreateView,
    CharacterDetailView,
    AllCharactersListView,
    CharacterDeleteView,
    CharacterUpdateView
)


urlpatterns = [
    path('movies/create', MovieListCreateView.as_view(), name='movie-create'),
    path('movies/details/<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/all', AllMoviesListView.as_view(), name='all-movies'),
    path('movies/delete/<int:pk>', MovieDeleteView.as_view(), name='movie-delete'),
    path('movies/update/<int:pk>', MovieUpdateView.as_view(), name='movie-update'),
    path('actors/create', ActorListCreateView.as_view(), name='actor-create'),
    path('actors/details/<int:pk>', ActorDetailView.as_view(), name='actor-detail'),
    path('actors/all', AllActorsListView.as_view(), name='all-actors'),
    path('actors/delete/<int:pk>', ActorDeleteView.as_view(), name='actor-delete'),
    path('actors/update/<int:pk>', ActorUpdateView.as_view(), name='actor-update'),
    path('characters/create', CharacterListCreateView.as_view(), name='character-create'),
    path('characters/details/<int:pk>', CharacterDetailView.as_view(), name='character-detail'),
    path('characters/all', AllCharactersListView.as_view(), name='all-characters'),
    path('characters/delete/<int:pk>', CharacterDeleteView.as_view(), name='character-delete'),
    path('characters/update/<int:pk>', CharacterUpdateView.as_view(), name='character-update'),
]
