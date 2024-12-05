from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from cinemabiggu.models import Session, Movie, Room, Genre
from cinemabiggu.serializers.sessions import SessionSerializer
from django.urls import reverse
from rest_framework import status


class SessionRequestsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='test_requests', password='test_requests'
        )
        self.client.force_authenticate(self.user)
        self.url = reverse('Sessions-list')
        self.genre = Genre.objects.create(
            name='Genre Test Movie',
            description='Genre Test Description'
        )
        self.movie = Movie.objects.create(
            title='Movie Test',
            description='This movie is a test',
            genre=self.genre,
            duration=120,
            release_date='2000-01-01',
            avaliable=True
        )
        self.room = Room.objects.create(
            room_id=1,
            capacity=100,
            imax=False
        )
        self.session_01 = Session.objects.create(
            movie=self.movie,
            room=self.room,
            start_time='2024-01-01T00:00:00Z',
            end_time='2024-01-01T02:00:00Z'
        )
        self.session_02 = Session.objects.create(
            movie=self.movie,
            room=self.room,
            start_time='2024-01-01T03:00:00Z',
            end_time='2024-01-01T05:00:00Z'
        )

    def test_request_get_sessions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_get_a_session(self):
        session_id = self.session_01.id
        response = self.client.get(f'{self.url}{session_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        session_data = Session.objects.get(pk=session_id)
        session_serialized_data = SessionSerializer(instance=session_data).data
        self.assertEqual(response.data, session_serialized_data)

    def test_request_post_session(self):
        data = {
            'movie': self.movie.id,
            'room': self.room.room_id,
            'start_time': '2024-01-01T06:00:00Z',
            'end_time': '2024-01-01T08:00:00Z'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        session_inserted = Session.objects.get(**data)
        session_serialized_data = SessionSerializer(instance=session_inserted).data
        self.assertEqual(response.data, session_serialized_data)

    def test_request_put_session(self):
        session_id = self.session_02.id
        data = {
            'movie': self.movie.id,
            'room': self.room.room_id,
            'start_time': '2024-01-01T10:00:00Z',
            'end_time': '2024-01-01T12:00:00Z'
        }
        response = self.client.put(f'{self.url}{session_id}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        session_inserted = Session.objects.get(**data)
        session_serialized_data = SessionSerializer(instance=session_inserted).data
        self.assertEqual(response.data, session_serialized_data)

    def test_request_delete_session(self):
        session_id = self.session_01.id
        response = self.client.delete(f'{self.url}{session_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f'{self.url}{session_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
