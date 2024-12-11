from rest_framework import serializers
from cinemabiggu.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name', 'description', 'movie', 'actor']
