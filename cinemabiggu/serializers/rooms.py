from rest_framework import serializers
from cinemabiggu.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_id', 'capacity', 'imax']
