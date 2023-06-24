from django.urls import path, include
from rest_framework import routers
from . import views

api_router = routers.DefaultRouter()
api_router.register(r'moment', views.MomentAPIView)
api_router.register(r'moment_vote', views.MomentVoteAPIView)

urlpatterns =[
   
 path('', include(api_router.urls)),
   
]