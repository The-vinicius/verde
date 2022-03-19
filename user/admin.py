from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, UserProfile


@admin.register(CustomUser)
class UserAdmin(auth_admin.UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]



@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile

