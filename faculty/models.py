from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=255, unique=True ,default="Faculty of science") 
    description = models.TextField(null=True, blank=True)
    head = models.OneToOneField('FacultyHead', on_delete=models.SET_NULL, null=True, related_name="head_of_faculty")
    
    def __str__(self):
        return self.name
    
class FacultyHead(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.OneToOneField(Faculty, on_delete=models.CASCADE, related_name='head_of_faculty', null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"
        
    