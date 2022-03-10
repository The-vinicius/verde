from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, UserImageForm
from .models import UserProfile
User = get_user_model()


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



class UserProfileView(View):
    def get(self,request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)
        profile = UserProfile.objects.get(user=user)

        context = {
                'user': user,
                'profile':profile
        }

        return render(request, 'profile/detail.html', context)




@login_required
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