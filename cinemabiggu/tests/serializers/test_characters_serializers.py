from django.test import TestCase
from cinemabiggu.models import Character, Movie, Actor, Genre
from cinemabiggu.serializers import CharacterSerializer


class CharacterSerializerTestCase(TestCase):
    def setUp(self):
        self.genre = Genre(
            name='Genre Test Character',
            description='Genre Test Description'
        )
        self.movie = Movie(
            title='Movie Test Character',
            description='This movie is a test',
            genre=self.genre,
            duration=120,
            release_date='2000-01-01',
            avaliable=True
        )
        self.actor = Actor(
            name='Actor Test Character',
            description='This actor is a test',
            birth_date='2000-01-01',
            awards=[]
        )
        self.character = Character(
            name='Character Test',
            description='This character is a test',
            movie=self.movie,
            actor=self.actor
        )
        self.character_serializer = CharacterSerializer(instance=self.character)

    def test_character_keys(self):
        data = self.character_serializer.data
        character_fields = set([
            'id', 'name', 'description',
            'movie', 'actor'
        ])
        self.assertEqual(
            set(data.keys()),
            character_fields
        )

    def test_character_values(self):
        data = self.character_serializer.data
        self.assertEqual(data['name'], self.character.name)
        self.assertEqual(data['description'], self.character.description)
        self.assertEqual(data['movie'], self.movie.id)
        self.assertEqual(data['actor'], self.actor.id)
