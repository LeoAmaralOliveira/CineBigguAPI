from django.db import models


class Session(models.Model):
    movie = models.ForeignKey('cinemabiggu.Movie', on_delete=models.CASCADE)
    room = models.ForeignKey('cinemabiggu.Room', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.movie} - {self.room} - {self.start_time}'
