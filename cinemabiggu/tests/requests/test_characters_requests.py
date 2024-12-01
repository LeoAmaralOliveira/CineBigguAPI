from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from cinemabiggu.models import Character, Movie, Actor, Genre
from cinemabiggu.serializers import CharacterSerializer


class CharacterRequestsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='test_requests', password='test_requests'
        )
        self.url = reverse('Characters-list')
        self.client.force_authenticate(self.user)
        self.genre = Genre.objects.create(
            name='Genre Test Request Character',
            description='This genre is a test'
        )
        self.movie = Movie.objects.create(
            title='Movie Request Test Character',
            description='This movie is a test',
            genre=self.genre,
            duration=120,
            release_date='2000-01-01',
            avaliable=True
        )
        self.actor = Actor.objects.create(
            name='Actor Request Test Character',
            description='This actor is a test',
            birth_date='2000-01-01',
            awards=[]
        )
        self.character_01 = Character.objects.create(
            name='Character Request Test 1',
            description='This character is a test',
            movie=self.movie,
            actor=self.actor
        )
        self.character_02 = Character.objects.create(
            name='Character Request Test 2',
            description='This character is a test',
            movie=self.movie,
            actor=self.actor
        )

    def test_request_get_characters(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_a_character(self):
        character_id = self.character_01.id
        response = self.client.get(f'{self.url}{character_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        character_data = Character.objects.get(pk=character_id)
        character_serialized_data = CharacterSerializer(instance=character_data).data
        self.assertEqual(response.data, character_serialized_data)

    def test_request_post_character(self):
        data = {
            'name': 'Character Request Test 3',
            'description': 'This character is a test',
            'movie': self.movie.id,
            'actor': self.actor.id
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        character_inserted = Character.objects.get(**data)
        character_serialized_data = CharacterSerializer(instance=character_inserted).data
        self.assertEqual(response.data, character_serialized_data)

    def test_request_delete_a_character(self):
        character_id = self.character_02.id
        response = self.client.delete(f'{self.url}{character_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f'{self.url}{character_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_request_put_character(self):
        data = {
            'name': 'Character Request Test 4',
            'description': 'This character is a test',
            'movie': self.movie.id,
            'actor': self.actor.id
        }
        character_id = self.character_01.id
        response = self.client.put(f'{self.url}{character_id}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        character_inserted = Character.objects.get(**data)
        character_serialized_data = CharacterSerializer(instance=character_inserted).data
        self.assertEqual(response.data, character_serialized_data)
