from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=75,
        blank=False,
        null=False,
        unique=True
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
