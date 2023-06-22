from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator

from .models import User

from .serializers import (UserSerializer, LoginSerializer)

from rest_framework import viewsets, mixins, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action



# Create your views here.

class RegisterAPIView(APIView):
    def post(self, request, **extra_fields):
        profile_id = request.data.get('profile_id')
        username = request.data.get('username') 
        password = request.data.get('password')
        profile_image = request.data.get('profile_img')
        bio = request.data.get('bio')
        is_wallet_user = request.data.get('is_wallet_user')
        accept_terms = request.data.get('accept_terms')
        confirmation = request.data.get('confirmation')

        if not accept_terms:
            return Response(
                {"message": "You must accept the terms of service."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if password != confirmation:
            return Response(
                {"message": "Passwords must match."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.create_user(profile_id, password, username **extra_fields)
            user = authenticate(request, profile_id=profile_id, username=username, password=password)
            user.save()
            return Response(
                {"message": "Account created."},
                status=status.HTTP_201_CREATED
            )
        except IntegrityError:
            return Response(
                {"message": "Username already taken."},
                status=status.HTTP_400_BAD_REQUEST
            )
             
class LoginAPIView(APIView):
    def get(self, request):
        serializer = LoginSerializer(request.user)
        return Response(serializer.data)
    
    def post(self,request):
        username_or_profile_id = request.data.get("username/profile_id")
        password = request.data.get("password")
        user = authenticate(request, username=username_or_profile_id, password=password)

        if user is not None:
            login(request, user)
            return Response(
                    {"message": "User Found."},
                    status=status.HTTP_200_OK
                )

def logout_view(request):
    logout(request)
    return Response(
                    {"message": "Logged Out."},
                    status=status.HTTP_200_OK
                )

class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    def patch(self, request):
        # print(request.data)
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        # print(serializer.initial_data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=204)
        # print(serializer.errors)
        return Response(status=400)