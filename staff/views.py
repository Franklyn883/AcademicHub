# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import StaffRegistrationSerializer

class StaffRegistrationView(generics.CreateAPIView):
    """This view creates a student user."""
    serializer_class = StaffRegistrationSerializer
    permission_classes = [AllowAny]
    
