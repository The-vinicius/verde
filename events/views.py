from django.views.generic import ListView, DetailView

from .models import Event


class EventListView(ListView):
	queryset = Event.objects.all() 
	template_name = "events/events_list.html"


	def get_context_data(self, *args, **kwargs):
		context = super(EventListView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

class EventDetailSlugView(DetailView):
	template_name = "events/events_detail.html"