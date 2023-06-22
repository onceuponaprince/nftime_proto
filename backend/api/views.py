from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MomentVote, Moment
from .serializers import (MomentUserSerializer, MomentVoteSerializer)
from django.db.models import Count

from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator

from .exceptions import CannotActionOtherUserInfoError

MAX_PAGE_LENGTH = 10

# Create your views here.

class MomentAPIView(viewsets.ModelViewSet):
    queryset = Moment.objects.all()
    pages = 0

    def get_queryset(self):
        queryset = Moment.objects.all()
        
        queryset = queryset.order_by('-created_at')
       
        
        # Moments' Pagination
        page = self.request.query_params.get('page', 1)
        paginator = Paginator(queryset, MAX_PAGE_LENGTH)
        queryset = paginator.get_page(page)
        self.pages = paginator.num_pages
        return queryset
    
    def top_voted(self):
        top_moments = Moment.objects.all().annotate(num_posts=Count('momentvote')).order_by('-num_posts')
    def perform_create(self, serializer):
        kwargs = {
            'user': self.request.user, 
            'title': serializer.validated_data['title'],
            'desc': serializer.validated_data['desc'],
            'image': serializer.validated_data['image'],
        }
        serializer.save(**kwargs)
    
    def perform_destroy(self, instance):
        moment = self.get_object()
        # disable delete other user' tweets
        if (moment.user != self.request.user):
            return Response(
                {"message": "You can't do that!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        instance.delete()

class MomentVoteAPIView(viewsets.ModelViewSet):
    queryset = MomentVote.objects.all()

    def get_queryset(self):
        queryset = MomentVote.objects.all()


    def get_vote_count(self):
        queryset = MomentVote.objects.all()

        for moment in queryset:
            likes_set = MomentVote.objects.filter(moment=moment['id'])
            moment['likes_count'] = likes_set.count()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MomentVoteSerializer
        else:
            return None

    def perform_create(self, serializer):
        kwargs = {
            'user': self.request.user, 
            'moment': serializer.validated_data['moment']
        }
        serializer.save(**kwargs)
    
    def perform_destroy(self, instance):
        momentVote = self.get_object()
        
        if (momentVote.user != self.request.user):
            raise CannotActionOtherUserInfoError(action='delete', info='moments')
        instance.delete()