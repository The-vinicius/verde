from django.db import models
from green.utils import unique_slug_generator
from django.db.models.signals import pre_save
from auditlog.registry import auditlog
from autoslug import AutoSlugField


class Event(models.Model):
	title = models.CharField(max_length=255)
	slug = AutoSlugField(unique=True, always_update=False, populate_from="title")
	description = models.TextField()
	active      = models.BooleanField(default = False)
	timestamp   = models.DateTimeField(auto_now_add = True)


	def __str__(self):
		return self.title

# registro de auditoria

auditlog.register(Event)

def event_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(event_pre_save_receiver, sender=Event)