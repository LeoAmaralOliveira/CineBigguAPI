from django.db import models


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
