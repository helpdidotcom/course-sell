from django.db import models
from .course import Course


class Video(models.Model):
    serial_number = models.IntegerField(null=False)
    title = models.CharField(null=False, max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video_id = models.CharField(null=False, max_length=30)
    is_preview = models.BooleanField(default=False)

    def __str__(self):
        return self.title
