# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import authentication, userhome

app_name = 'user'

urlpatterns = [
    path('', authentication, name='authentication'),
    path('home/', userhome, name='userhome'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Ensure the correct name is used
    # Add other URLs as needed
]
