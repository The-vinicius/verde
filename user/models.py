from django.contrib.auth.models import AbstractUser
from django.db import models
from events.models import Event

class UserQuerySet(models.query.QuerySet):
    def events_user(self, user):
        return Event.objects.filter(participantes=user)

class UserManager(models.Manager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def event_set(self, user):
        return self.get_queryset().events_user(user)


class CustomUser(AbstractUser):
    objects = UserManager()


    def __str__(self):
        return self.username