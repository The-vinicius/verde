from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.shortcuts import render

from .forms import CustomUserCreationForm, UserImageForm
from .models import UserProfile


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def user_profile_view(request, name):
    profile = UserProfile.objects.get_or_new(request)
    
    if request.method == 'POST':

        form = UserImageForm(request.POST, request.FILES)

        if form.is_valid():
            profile.image = form.cleaned_data['image']
            profile.save()
    else:
        form = UserImageForm()

    context = {
            'form':form,
            'profile': profile
    }

    return render(request, 'profile/profile.html', context)