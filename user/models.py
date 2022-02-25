from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from events.models import Event

class UserQuerySet(models.query.QuerySet):
    def events_user(self, user):
        return Event.objects.filter(participantes=user)

class UserManager(UserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def event_set(self, user):
        return self.get_queryset().events_user(user)

# custom user
class CustomUser(AbstractUser):
    objects = UserManager()


    def __str__(self):
        return self.username




# user profile

class UserProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='user/img/', null=True, blank=True)
