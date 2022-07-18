from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50, null=False)
    slug = models.CharField(max_length=50, null=False, unique=True)
    description = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    length = models.IntegerField(null=False)
    image = models.ImageField(upload_to='files/thumbnail')
    resource = models.FileField(upload_to='files/resource')

    def __str__(self):
        return self.name


def get_course_by_slug(slug):
    return Course.objects.get(slug=slug)
