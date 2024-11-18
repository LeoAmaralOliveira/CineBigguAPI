from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from django.contrib.auth import get_user_model
from cinemabiggu.views import MovieViewSet


class CinuemabigguTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpass'
        )

    def test_list_movies(self):
        request = self.factory.get('/api/v1/movies')
        force_authenticate(request, user=self.user)
        self.assertEqual(
            MovieViewSet.as_view({'get': 'list'})(request).status_code, 200
        )
