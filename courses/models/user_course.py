from django.db import models
from django.contrib.auth.models import User
from .course import Course

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user)