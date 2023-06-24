from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_id', 'username', 'bio')
        

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_id', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}