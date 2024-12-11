from django.test import TestCase
from cinemabiggu.models import Movie, Genre
from cinemabiggu.serializers import MovieSerializer


class MovieSerializerTestCase(TestCase):
    def setUp(self):
        self.genre = Genre(
            name='Genre Test Movie',
            description='Genre Test Description'
        )
        self.movie = Movie(
            title='Movie Test',
            description='This movie is a test',
            genre=self.genre,
            duration=120,
            release_date='2000-01-01',
            avaliable=True
        )
        self.movie_serializer = MovieSerializer(instance=self.movie)

    def test_movie_keys(self):
        data = self.movie_serializer.data
        movie_fields = set([
            'id', 'title', 'description',
            'genre', 'duration', 'release_date',
            'avaliable'
        ])
        self.assertEqual(
            set(data.keys()),
            movie_fields
        )

    def test_movie_values(self):
        data = self.movie_serializer.data
        self.assertEqual(data['title'], self.movie.title)
        self.assertEqual(data['description'], self.movie.description)
        self.assertEqual(data['genre'], self.genre.id)
        self.assertEqual(data['duration'], self.movie.duration)
        self.assertEqual(data['release_date'], self.movie.release_date)
        self.assertEqual(data['avaliable'], self.movie.avaliable)
