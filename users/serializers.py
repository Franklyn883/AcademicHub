from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer,UserSerializer
from rest_framework.exceptions import ValidationError   

#custom user
User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email', 'first_name','last_name','password')  # Exclude 'username'
    



