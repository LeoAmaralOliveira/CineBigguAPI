from rest_framework import serializers
from cinemabiggu.models import Session


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'movie', 'room', 'start_time', 'end_time']
