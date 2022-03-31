from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm, EditProfileForm
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
def edit_profile(request):
    user = request.user.id
    profile = UserProfile.objects.get(user__id=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            profile.image = form.cleaned_data.get('image')
            profile.bio   = form.cleaned_data.get('bio')
            profile.gender = form.cleaned_data.get('gender')
            profile.wallet = form.cleaned_data.get('wallet')
            profile.save() 

            return redirect('accounts:profile', username=request.user.username)
    else:
        form = EditProfileForm(instance=profile)


    context = {
        'form': form,
        'profile':profile
    }


    return render(request, 'profile/profile.html', context)