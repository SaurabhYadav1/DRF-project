from django.db import models


class Student(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    address = models.CharField(max_length=60)