from django.test import TestCase
from cinemabiggu.models import Room
from cinemabiggu.serializers import RoomSerializer


class RoomSerializerTestCase(TestCase):
    def setUp(self):
        self.room = Room(
            room_id=1,
            capacity=100,
            imax=False
        )
        self.room_serializer = RoomSerializer(instance=self.room)

    def test_room_keys(self):
        data = self.room_serializer.data
        room_fields = set([
            'room_id', 'capacity', 'imax'
        ])
        self.assertEqual(
            set(data.keys()),
            room_fields
        )

    def test_room_values(self):
        data = self.room_serializer.data
        self.assertEqual(data['room_id'], self.room.room_id)
        self.assertEqual(data['capacity'], self.room.capacity)
        self.assertEqual(data['imax'], self.room.imax)
