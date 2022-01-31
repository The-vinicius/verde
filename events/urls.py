from django.urls import path
from .views import EventDetailSlugView, EventListView, add_user_event


app_name = 'events'


urlpatterns = [
	path('', EventListView.as_view(), name='list'),
	path('<slug:slug>/', EventDetailSlugView.as_view(), name='detail'),
	path('add_user/', add_user_event, name='add_user')
	]