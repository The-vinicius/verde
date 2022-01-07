from django.urls import path
from .views import HomePage

app_name = 'pages'


urlpatterns = [
	path('home/', HomePage.as_view(), name='home'),
]