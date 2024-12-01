from django.db import models


class Movie(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        unique=True
    )
    description = models.TextField()
    genre = models.ForeignKey('cinemabiggu.Genre', on_delete=models.CASCADE)
    duration = models.IntegerField(null=True, blank=True)
    release_date = models.DateField()
    avaliable = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
