from django.db import models


# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    credit_hours = models.IntegerField()
    department = models.ForeignKey('department.Department', on_delete=models.SET_NULL, related_name='courses', null=True)
    
    def __str__(self):
        return self.title