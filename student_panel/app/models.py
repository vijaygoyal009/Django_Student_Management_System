from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=255)


class AddCourses(models.Model):
    course = models.CharField(max_length=100)
    fees = models.IntegerField()
    duration = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)