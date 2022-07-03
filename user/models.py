from django.db import models
from django.contrib.auth.models import AbstractUser

from room.models import Room

# Create your models here.


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='static/avatars/%Y/%m/')
