from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.
class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id =models.CharField(max_length=10, unique=True)
    qualification = models.CharField(max_length=255)
    department = models.ForeignKey('department.Department', on_delete=models.SET_NULL, null=True)
    courses = models.ManyToManyField('courses.Course', related_name='faculty')
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    