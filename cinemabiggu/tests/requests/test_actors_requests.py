from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from cinemabiggu.models import Actor
from cinemabiggu.serializers import ActorSerializer


class ActorRequestsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='test_requests', password='test_requests'
        )
        self.url = reverse('Actors-list')
        self.client.force_authenticate(self.user)
        self.actor_01 = Actor.objects.create(
            name='Actor Request Test',
            description='This actor is a test',
            birth_date='2000-01-01',
            awards=[]
        )
        self.actor_02 = Actor.objects.create(
            name='Actor Request Test 2',
            description='This actor is a test',
            birth_date='2000-01-01',
            awards=[]
        )

    def test_request_get_actors(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_a_actor(self):
        actor_id = self.actor_01.id
        response = self.client.get(f'{self.url}{actor_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        actor_data = Actor.objects.get(pk=actor_id)
        actor_serialized_data = ActorSerializer(instance=actor_data).data
        self.assertEqual(response.data, actor_serialized_data)

    def test_request_post_actor(self):
        data = {
            'name': 'Actor Request Test 3',
            'description': 'This actor is a test',
            'birth_date': '2000-01-01',
            'awards': '[]'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        actor_inserted = Actor.objects.get(name=data['name'])
        actor_serialized_data = ActorSerializer(instance=actor_inserted).data
        self.assertEqual(response.data, actor_serialized_data)

    def test_request_delete_a_actor(self):
        actor_id = self.actor_02.id
        response = self.client.delete(f'{self.url}{actor_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f'{self.url}{actor_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_request_put_actor(self):
        data = {
            'name': 'Actor Request Test 4',
            'description': 'This actor is a test',
            'birth_date': '2000-01-01',
            'awards': '[]'
        }
        actor_id = self.actor_01.id
        response = self.client.put(f'{self.url}{actor_id}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        actor_inserted = Actor.objects.get(name=data['name'])
        actor_serialized_data = ActorSerializer(instance=actor_inserted).data
        self.assertEqual(response.data, actor_serialized_data)
