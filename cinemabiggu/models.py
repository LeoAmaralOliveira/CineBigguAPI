from django.db import models


class Movie(models.Model):
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        unique=True
    )
    description = models.TextField()
    genre = models.CharField(max_length=80)
    duration = models.IntegerField(null=True, blank=True)
    release_date = models.DateField()
    avaliable = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(
        max_length=120, blank=False, null=False, unique=True
    )
    description = models.TextField()
    birth_date = models.DateTimeField()
    awards = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
