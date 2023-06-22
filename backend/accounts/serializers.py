from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_id', 'user_name', 'password', 'profile_img', 'bio', 'is_wallet_user', 'accept_terms')
        extra_kwargs = {'password': {'write_only': True}}

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_id', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}