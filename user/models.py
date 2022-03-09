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

class ProfileManager(models.Manager):
    def get_or_new(self, request):
        user = request.user
        qs = self.get_queryset().filter(user=user)
        if qs.count() == 1:
            return user.userprofile
        else:
            return self.model.objects.create(user=user)


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='user/img/', null=True, blank=True)
    objects = ProfileManager()

    def __str__(self):
        return self.user.username