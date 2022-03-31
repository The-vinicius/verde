from django.urls import path
from .views import SignUpView, edit_profile, UserProfileView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/view/<str:username>/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', edit_profile, name='edit-profile')
]