"""Define the URL patterns for the users app."""
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'
urlpatterns = [
    # Include the default auth URLs provided by Django
    path('', include('django.contrib.auth.urls')),
    # User registration page
    path('register/', views.register, name='register'),
    # path('logout/', views.logoutUser, name='logout'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
]

#te