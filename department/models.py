from django.db import models
from faculty.models import Faculty
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)
    head_of_department = models.OneToOneField('DepartmentHead', on_delete=models.SET_NULL, related_name="department_head", null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="departments", null=True)
    
    def __str__(self):
        return self.name
    
class DepartmentHead(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    department = models.OneToOneField(Department, on_delete=models.CASCADE, related_name="head_of")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"