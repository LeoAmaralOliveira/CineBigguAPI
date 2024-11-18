from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField()
    movie = models.ForeignKey('cinemabiggu.Movie', on_delete=models.CASCADE)
    actor = models.ForeignKey('cinemabiggu.Actor', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
