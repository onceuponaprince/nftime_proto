from django.urls import path, include
from . import views



urlpatterns = [
    path('register', views.registration_view, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('current_user', views.current_user_view, name='current_user'),
]