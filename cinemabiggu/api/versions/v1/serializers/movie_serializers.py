from rest_framework import serializers
from cinemabiggu.api.models.movie import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
