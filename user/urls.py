from django.urls import path
from .views import SignUpView, user_profile_view, UserProfileView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/view/<str:username>/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/<str:name>/', user_profile_view, name='edit-profile')
]