from rest_framework import serializers
from .models import Moment, MomentVote
from accounts.serializers import UserSerializer

class MomentVoteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = MomentVote
        fields = ('id', 'user', 'moment', 'created_at')
    
    def create(self, validated_data):
        vote, created = MomentVote.objects.get_or_create(
            user=validated_data['user'], 
            moment=validated_data['moment'],
            defaults={'created_at': validated_data.get('created_at', None)}
        )
        return vote

class MomentUserSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    votes = MomentVoteSerializer(many=True, read_only=True)
    class Meta:
        model = Moment
        fields = ('id', 'user', 'title', 'desc', 'image', 'is_minted', 'votes', 'created_at')

    def create(self, validated_data):
        moment = Moment.objects.create(
            user=validated_data['user'], 
            title=validated_data['title'],
            desc=validated_data['desc'],
            image=validated_data['image'],
        )
        return moment
