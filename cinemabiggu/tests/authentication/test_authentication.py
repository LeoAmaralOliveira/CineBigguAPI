from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import authenticate
from django.urls import reverse


class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='test', password='test'
        )
        self.url = reverse('Movies-list')

    def test_correct_authentication(self):
        user = authenticate(username='test', password='test')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_incorrect_username_authentication(self):
        user = authenticate(username='tes', password='test')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_incorrect_password_authentication(self):
        user = authenticate(username='test', password='tes')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_request_get_authorized(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_unauthorized(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
