from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
def upload_to(instance,filename):
    return 'images/{filename}.format(filename=filename)'

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=255)
    last_name = models.CharField(_("last name"), max_length=255)
    location = models.CharField(_("location"), max_length=255, null=True, blank=True),
    gender_choices =[
        ('M', 'Male'),
        ('F', 'Female')
    ]
    role_choices =[
        ('A', 'Admin'),
        ('S', 'Student'),
        ('SF', 'Staff')
    ]
    gender = models.CharField(max_length=1, choices=gender_choices,null=True, blank=True)
    role = models.CharField(max_length=2, choices = role_choices, null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True) 
    image_url = models.ImageField(upload_to=upload_to, null=True)
    date_of_birth = models.DateField(null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"