from django.test import TestCase
from cinemabiggu.models import Session, Movie, Genre, Room
from cinemabiggu.serializers import SessionSerializer


class TestSessionSerializer(TestCase):
    def setUp(self):
        self.genre = Genre(
            name='Genre Test Movie',
            description='Genre Test Description'
        )
        self.movie = Movie(
            title='Movie Test',
            description='This movie is a test',
            genre=self.genre,
            duration=120,
            release_date='2000-01-01',
            avaliable=True
        )
        self.room = Room(
            room_id=1,
            capacity=100,
            imax=False
        )
        self.session = Session(
            movie=self.movie,
            room=self.room,
            start_time='2024-01-01T00:00:00Z',
            end_time='2024-01-01T02:00:00Z'
        )
        self.session_serializer = SessionSerializer(instance=self.session)

    def test_session_keys(self):
        data = self.session_serializer.data
        session_fields = set([
            'id', 'movie', 'room', 'start_time',
            'end_time', 'created_at', 'updated_at'
        ])
        self.assertEqual(
            set(data.keys()),
            session_fields
        )

    def test_session_values(self):
        data = self.session_serializer.data
        self.assertEqual(data['movie'], self.movie.id)
        self.assertEqual(data['room'], self.room.room_id)
        self.assertEqual(data['start_time'], self.session.start_time)
        self.assertEqual(data['end_time'], self.session.end_time)
