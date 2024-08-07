# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import StudentRegistrationSerializer

class StudentRegistrationView(generics.CreateAPIView):
    """This view creates a student user."""
    serializer_class = StudentRegistrationSerializer
    permission_classes = [AllowAny]
    
