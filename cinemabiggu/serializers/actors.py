from rest_framework import serializers
from cinemabiggu.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'description', 'birth_date', 'awards']
