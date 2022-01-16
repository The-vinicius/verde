from django.urls import path
from .views import EventDetailSlugView, EventListView


app_name = 'events'


urlpatterns = [
	path('', EventListView.as_view(), name='list')
	]