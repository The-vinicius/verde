from django.views.generic import ListView, DetailView
from django.http import Http404
from .models import Event


class EventListView(ListView):
	queryset = Event.objects.all() 
	template_name = "events/events_list.html"


	def get_context_data(self, *args, **kwargs):
		context = super(EventListView, self).get_context_data(*args, **kwargs)
		return context

class EventDetailSlugView(DetailView):
	queryset = Event.objects.all()
	template_name = "events/events_detail.html"


	def get_context_data(self, *args, **kwargs):
		context = super(EventDetailSlugView, self).get_context_data(*args, **kwargs)
		return context

	def get_object(self, *args, **kwargs):
		slug = self.kwargs.get('slug')

		try:
			instace = Event.objects.get(slug = slug)
		except Event.DoesNotExist:
			raise Http404('Não encontrado!')
		except Event.MultipleObjectsReturned:
			qs = Event.objects.filter(slug = slug)
			instace = qs.first()
		return instace