from rest_framework import serializers
from .models import Moment, MomentVote
from accounts.serializers import UserSerializer

class MomentUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Moment
        fields = ('id', 'user', 'title', 'desc', 'image', 'created_at')

class MomentVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MomentVote
        fields = ('id', 'user', 'tweet', 'created_at')