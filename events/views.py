from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render 
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Event
from user.models import CustomUser
from django.utils.http import url_has_allowed_host_and_scheme


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
		slug = self.kwargs.get('slug')
		qs = self.get_object()
		context['total'] = qs.participantes.count()
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


	def post(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return add_user_event(request)
		else:
			return redirect('/accounts/login/')

def add_user_event(request):
	slug = request.POST.get('slug')
	user_id = request.POST.get('user_id')

	#url redirect
	next_post = request.POST.get('next')
	next_get = request.GET.get('next')
	redirect_path = next_get or next_post or None

	if user_id is not None:
		try:
			user_entry = CustomUser.objects.get(id=user_id)
		except CustomUser.DoesNotExist:
			redirect('/login/')
		else:
			qs = Event.objects.get(slug=slug)
			qs.participantes.add(user_entry)
		if url_has_allowed_host_and_scheme(redirect_path, request.get_host()):
			return redirect(redirect_path)

	return Redirect('/events/')