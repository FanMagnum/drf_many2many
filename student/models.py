'''
Author: Lone
Date: 2020-11-28 16:24:50
LastEditTime: 2020-11-28 17:04:41
FilePath: /many2many/student/models.py
'''
from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=20)
    
class Student(models.Model):
    name = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course)