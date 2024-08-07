from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import StudentProfile

User = get_user_model()

class StudentRegistrationSerializer(UserCreateSerializer):
    """custom serializer to handle student registration."""
    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields =("id","password","first_name", "last_name","email",)
        
    def create(self,validated_data):
        """Create a student user."""
        user = User.objects.create_user(**validated_data, is_student=True)
        StudentProfile.objects.create(user=user)
        
        return user
        
        