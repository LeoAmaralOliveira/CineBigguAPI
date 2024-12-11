from rest_framework import serializers
from cinemabiggu.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'description',
            'genre',
            'duration',
            'release_date',
            'avaliable'
        ]
