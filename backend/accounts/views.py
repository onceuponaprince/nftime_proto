from django.shortcuts import render
from django.http import JsonResponse
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
from django_nextjs.render import render_nextjs_page_sync
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def registration_view(request):
   print(request)
   if request.method == 'GET':
        return JsonResponse({"message": "Method not allowed"}, status=405)
   if request.method == 'POST':
    profile_id = request.POST.get('profile_id', '')
    username = request.POST.get('username', '')
    bio = request.POST.get('bio', '')
    print(f"profile_id: {profile_id}")
    print(f"username: {username}")

    if not profile_id:
        return JsonResponse(
            {"message": "Profile ID must be provided"},
            status=400
        )
    if not username:
        return JsonResponse(
            {"message": "Username must be provided"},
            status=400
        )

    try:
        user = User.objects.create_user(profile_id, username, bio)
        user.save()
        return JsonResponse(
            {"message": "Account created."},
            status=201
        )
    except IntegrityError:
        return JsonResponse(
            {"message": "Username already taken."},
            status=400
        )
    
def login_view(request):
    if request.method == 'GET':
        return JsonResponse({"message": "Method not allowed"}, status=405)

    username_or_profile_id = request.POST.get("username/profile_id")
    password = ""
    user = authenticate(request, username=username_or_profile_id, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse(
            {"message": "User Found."},
            status=200
        )
    else:
        return JsonResponse(
            {"message": "Invalid credentials."},
            status=400
        )

def logout_view(request):
    logout(request)
    return JsonResponse(
        {"message": "Logged Out."},
        status=200
    )

def current_user_view(request):
    if request.method == 'GET':
        serializer = UserSerializer(request.user)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PATCH':
        serializer = UserSerializer(request.user, data=request.POST, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(status=204)
        else:
            return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)