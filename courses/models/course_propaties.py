from django.db import models
from .course import Course


class Couse_Propaties(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    desc = models.CharField(max_length=255, null=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.desc


class Tag(Couse_Propaties):
    pass


class Prerequisite(Couse_Propaties):
    pass


class Learning(Couse_Propaties):
    pass
