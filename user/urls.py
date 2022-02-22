from django.urls import path
from .views import SignUpView, UserProfile

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', UserProfile.as_view(), name='profile')
]