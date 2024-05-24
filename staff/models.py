from django.db import models
from django.contrib.auth import get_user_model
from department.models import Department
from courses.models import Course

User = get_user_model()
# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=True)
    teacher_id = models.CharField(max_length=10, unique=True)
    qualification = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    courses = models.ManyToManyField(Course, related_name='teachers')

    def save(self, *args, **kwargs):
        if not self.teacher_id:
            self.teacher_id = self.generate_teacher_id()
        super(Teacher, self).save(*args, **kwargs)

    def generate_teacher_id(self):
        last_teacher = Teacher.objects.all().order_by('id').last()
        if not last_teacher:
            return 'T0001'
        teacher_id = last_teacher.teacher_id
        teacher_int = int(teacher_id.split('T')[-1])
        new_teacher_int = teacher_int + 1
        new_teacher_id = 'T' + str(new_teacher_int).zfill(4)
        return new_teacher_id

    def __str__(self):
        return f"{self.title} {self.user.first_name} {self.user.last_name}"