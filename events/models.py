from django.db import models
from django.urls import reverse
from green.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.conf import settings
from auditlog.registry import auditlog
from autoslug import AutoSlugField


User = settings.AUTH_USER_MODEL

class Event(models.Model):
	admin = models.ForeignKey(User, related_name='admin', on_delete=models.CASCADE, blank=True, null=True)
	participantes = models.ManyToManyField(User,related_name='participantes', blank=True)
	title = models.CharField(max_length=255)
	slug = AutoSlugField(unique=True, always_update=False, populate_from="title")
	description = models.TextField()
	image = models.ImageField(upload_to='event/img/', blank=True, null=True)
	active      = models.BooleanField(default = False)
	timestamp   = models.DateTimeField(auto_now_add = True)
	start_date = models.DateTimeField(auto_now=False)
	end_date = models.DateTimeField(auto_now=False)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('events:detail', kwargs={'slug': self.slug})

# registro de auditoria

auditlog.register(Event)