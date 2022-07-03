from django.db import models
from django.contrib.auth import get_user_model

from room.models import Room

# Create your models here.
class ActivePostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Post(models.Model):
    content = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    seen_users = models.ManyToManyField(get_user_model(), related_name='seen_users')
    active = models.BooleanField(default=True)

    objects = models.Manager()
    active_posts = ActivePostManager()

    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return self.content[:100] + '...'

