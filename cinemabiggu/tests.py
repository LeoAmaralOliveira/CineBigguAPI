from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from django.contrib.auth import get_user_model
from cinemabiggu.views import MovieViewSet
from datetime import date
import json


class CinuemabigguTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpass'
        )

    def test_list_movies(self):
        view = MovieViewSet.as_view({'get': 'list'})
        request = self.factory.get('/api/v1/movies')
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(
            response.status_code, 200
        )

    def test_insert_movies(self):
        view = MovieViewSet.as_view({'post': 'dict'})
        request = self.factory.post(
            '/api/v1/movies/',
            json.dumps({
                "title": "test",
                "description": "test",
                "genre": "test",
                "duration": 1,
                "release_date": str(date.today()),
                "avaliable": True
            }),
            content_type='application/json'
        )
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertEqual(
            response.status_code, 201
        )
