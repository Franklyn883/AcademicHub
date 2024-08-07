from django.urls import path
from .views import (StaffRegistrationView)

urlpatterns = [
    path("staff", StaffRegistrationView.as_view()),
]