from django.test import TestCase
from cinemabiggu.models import Genre
from cinemabiggu.serializers import GenreSerializer


class GenreSerializerTestCase(TestCase):
    def setUp(self):
        self.genre = Genre(
            name='Genre Test',
            description='This genre is a test'
        )
        self.genre_serializer = GenreSerializer(instance=self.genre)

    def test_genre_keys(self):
        data = self.genre_serializer.data
        genre_fields = set([
            'id', 'name', 'description'
        ])
        self.assertEqual(
            set(data.keys()),
            genre_fields
        )

    def test_genre_values(self):
        data = self.genre_serializer.data
        self.assertEqual(data['name'], self.genre.name)
        self.assertEqual(data['description'], self.genre.description)
