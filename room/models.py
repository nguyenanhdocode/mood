from uuid import uuid4
from django.db import models
# from django.contrib.auth.models import User
from mood.settings import AUTH_USER_MODEL

# Create your models here.

class Room(models.Model):
    uuid = models.UUIDField(default=uuid4())
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(AUTH_USER_MODEL, default=[])

    def __str__(self):
        return f'{self.name} ({self.uuid})'
