from django.urls import path
from .views import (StudentRegistrationView)

urlpatterns = [
    path("student", StudentRegistrationView.as_view()),
]