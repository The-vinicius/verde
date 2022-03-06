from django.urls import path
from .views import SignUpView, user_profile_view

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<str:name>/', user_profile_view, name='profile')
]