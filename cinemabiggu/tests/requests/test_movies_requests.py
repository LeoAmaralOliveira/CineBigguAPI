from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from cinemabiggu.models import Movie, Genre
from cinemabiggu.serializers import MovieSerializer


class MovieRequestsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='test_requests', password='test_requests'
        )
        self.url = reverse('Movies-list')
        self.client.force_authenticate(self.user)
        self.genre = Genre.objects.create(
            name='Genre Test Request Movie',
            description='This genre is a test'
        )
        self.movie_01 = Movie.objects.create(
            title='Movie Request Test',
            description='This movie is a test',
            genre=self.genre,
            duration=120,
            release_date='2000-01-01',
            avaliable=True
        )
        self.movie_02 = Movie.objects.create(
            title='Movie Request Test 2',
            description='This movie is a test',
            genre=self.genre,
            duration=120,
            release_date='2000-01-01',
            avaliable=True
        )

    def test_request_get_movies(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_a_movie(self):
        movie_id = self.movie_01.id
        response = self.client.get(f'{self.url}{movie_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        movie_data = Movie.objects.get(pk=movie_id)
        movie_serialized_data = MovieSerializer(instance=movie_data).data
        self.assertEqual(response.data, movie_serialized_data)

    def test_request_post_movie(self):
        data = {
            'title': 'Movie Request Test 3',
            'description': 'This movie is a test',
            'genre': self.genre.id,
            'duration': 120,
            'release_date': '2000-01-01',
            'avaliable': True
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        movie_inserted = Movie.objects.get(title=data['title'])
        movie_serialized_data = MovieSerializer(instance=movie_inserted).data
        self.assertEqual(response.data, movie_serialized_data)

    def test_request_delete_a_movie(self):
        movie_id = self.movie_02.id
        response = self.client.delete(f'{self.url}{movie_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f'{self.url}{movie_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_request_put_movie(self):
        data = {
            'title': 'Movie Request Test 4',
            'description': 'This movie is a test',
            'genre': self.genre.id,
            'duration': 120,
            'release_date': '2000-01-01',
            'avaliable': True
        }
        movie_id = self.movie_01.id
        response = self.client.put(f'{self.url}{movie_id}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        movie_inserted = Movie.objects.get(title=data['title'])
        movie_serialized_data = MovieSerializer(instance=movie_inserted).data
        self.assertEqual(response.data, movie_serialized_data)
