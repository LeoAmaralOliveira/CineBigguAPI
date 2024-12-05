from django.db import models


class Room(models.Model):
    room_id = models.IntegerField(unique=True, primary_key=True, null=False, blank=False)
    capacity = models.IntegerField()
    imax = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
