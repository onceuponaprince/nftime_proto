from django.urls import path, include
from . import views

urlpatterns=[
    path("new_user/", views.RegisterAPIView.as_view(), name="new-user"),
    path("welcome/", views.LoginAPIView.as_view(), name='welcome'), 
    path("signout/", views.logout_view, name="signout"),
    path("current_user/<str:profile_id>/", views.CurrentUserView.as_view(), name='current_user')
]