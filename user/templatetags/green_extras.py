from django import template
from user.models import CustomUser, UserProfile


register = template.Library()


@register.simple_tag()
def get_photo_user(request):
	profile, obj  = UserProfile.objects.get_or_create(user=request.user)

	if profile.image:
		return profile.image.url

	else:
		return '/static/img/149753.jpg'