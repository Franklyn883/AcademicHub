from django.db import models
from faculty.models import Faculty

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)
    head_of_department = models.OneToOneField(Faculty, on_delete=models.SET_NULL, related_name="departmental_head", null=True)
    
    def __str__(self):
        return self.name