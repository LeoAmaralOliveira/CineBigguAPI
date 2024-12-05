from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from cinemabiggu.models import Room
from cinemabiggu.serializers import RoomSerializer
from rest_framework import status
from django.urls import reverse


class RoomRequestsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='test_requests', password='test_requests'
        )
        self.client.force_authenticate(self.user)
        self.url = reverse('Rooms-list')
        self.room_01 = Room.objects.create(
            room_id=1,
            capacity=100,
            imax=False
        )
        self.room_02 = Room.objects.create(
            room_id=2,
            capacity=100,
            imax=False
        )

    def test_request_get_rooms(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_a_room(self):
        room_id = self.room_01.room_id
        response = self.client.get(f'{self.url}{room_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        room_data = Room.objects.get(pk=room_id)
        room_serialized_data = RoomSerializer(instance=room_data).data
        self.assertEqual(response.data, room_serialized_data)

    def test_request_post_room(self):
        data = {
            'room_id': 3,
            'capacity': 100,
            'imax': False
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        room_inserted = Room.objects.get(room_id=data['room_id'])
        room_serialized_data = RoomSerializer(instance=room_inserted).data
        self.assertEqual(response.data, room_serialized_data)

    def test_request_put_room(self):
        room_id = self.room_02.room_id
        data = {
            'room_id': 2,
            'capacity': 200,
            'imax': True
        }
        response = self.client.put(f'{self.url}{room_id}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        room_inserted = Room.objects.get(room_id=data['room_id'])
        room_serialized_data = RoomSerializer(instance=room_inserted).data
        self.assertEqual(response.data, room_serialized_data)

    def test_request_delete_room(self):
        room_id = self.room_01.room_id
        response = self.client.delete(f'{self.url}{room_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f'{self.url}{room_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
