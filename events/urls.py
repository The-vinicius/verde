from django.urls import path
from .views import EventDetailSlugView, EventListView


app_name = 'events'


urlpatterns = [
	path('', EventListView.as_view(), name='list'),
	path('<slug:slug>/', EventDetailSlugView.as_view(), name='detail')
	]