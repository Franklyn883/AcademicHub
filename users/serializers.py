from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer,UserSerializer
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#custom user
User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id','email', 'password')  # Exclude 'username'
    



class CustomUserSerializer(UserSerializer):
    
    image_url = serializers.ImageField(required=False)
    
    class Meta(UserSerializer.Meta):
        fields = ['id', 'first_name',
                  'last_name', 'email',
                  ]

    # this is where we send a request to slash me/ or auth/users
    def validate(self, attrs):
        validated_attr = super().validate(attrs)
        email = validated_attr.get('email')

        user = user.objects.get(email=email)

        if user.is_deactivated:
            raise ValidationError(
                'Account deactivated')

        if not user.is_active:
            raise ValidationError(
                'Account not activated')

        return validated_attr
    