from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from cinemabiggu.models import Genre
from cinemabiggu.serializers import GenreSerializer


class GenreRequestsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='test_requests', password='test_requests'
        )
        self.url = reverse('Genres-list')
        self.client.force_authenticate(self.user)
        self.genre_01 = Genre.objects.create(
            name='Genre Test Request 1',
            description='This genre is a test'
        )
        self.genre_02 = Genre.objects.create(
            name='Genre Test Request 2',
            description='This genre is a test'
        )

    def test_request_get_genres(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_a_genre(self):
        genre_id = self.genre_01.id
        response = self.client.get(f'{self.url}{genre_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        genre_data = Genre.objects.get(pk=genre_id)
        genre_serialized_data = GenreSerializer(instance=genre_data).data
        self.assertEqual(response.data, genre_serialized_data)

    def test_request_post_genre(self):
        data = {
            'name': 'Genre Test Request 3',
            'description': 'This genre is a test'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        genre_inserted = Genre.objects.get(name=data['name'])
        genre_serialized_data = GenreSerializer(instance=genre_inserted).data
        self.assertEqual(response.data, genre_serialized_data)

    def test_request_delete_a_genre(self):
        genre_id = self.genre_02.id
        response = self.client.delete(f'{self.url}{genre_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f'{self.url}{genre_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_request_put_genre(self):
        data = {
            'name': 'Genre Test Request 3',
            'description': 'This genre is a test'
        }
        genre_id = self.genre_01.id
        response = self.client.put(f'{self.url}{genre_id}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        genre_inserted = Genre.objects.get(name=data['name'])
        genre_serialized_data = GenreSerializer(instance=genre_inserted).data
        self.assertEqual(response.data, genre_serialized_data)
