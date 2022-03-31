from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.urls import reverse



# custom user
class CustomUser(AbstractUser):
    objects = UserManager()

    def __str__(self):
        return self.username


LEAGUE_OPTIONS = (
    ('L1', 'god'),
    ('L2', 'gold'),
    ('L3', 'silver'),
    ('L4', 'bronze'),
    ('L5', 'no league')
)


# user profile
class UserProfile(models.Model):

    LEAGUE_OPTIONS = (
    ('L1', 'god'),
    ('L2', 'gold'),
    ('L3', 'silver'),
    ('L4', 'bronze'),
    ('L5', 'no league')
    )

    GENDER_OPTIONS = (
        ('M', 'male'),
        ('F', 'female')
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='user/img/', null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    points = models.IntegerField(default=0, null=True, blank=True)
    ranking = models.IntegerField(default=0, null=True, blank=True)
    league = models.TextField(choices=LEAGUE_OPTIONS, default='L5', max_length=2, blank=True)
    gender = models.TextField(choices=GENDER_OPTIONS, default='M', max_length=1, blank=True)
    wallet = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'username': self.user.username})