from django.db import models
from django.contrib.auth.models import User
from mongoengine import *

# Create your models here.
class Students(models.Model):
    studentId =models.CharField(max_length = 20)
    first_name =models.CharField(max_length = 30)
    last_name =models.CharField(max_length = 30)
    email =models.CharField(max_length = 30)

class Course(models.Model):
    courseId =models.CharField(max_length =255)
    coursename =models.CharField(max_length =255)


class Chapters(models.Model):
    chapterId =models.CharField(max_length =255)
    courseId =models.CharField(max_length =255)
    chaptertitle =models.CharField(max_length =255)
    Description = models.CharField(max_length =255)


class Chat(models.Model):
    sender =models.CharField(max_length =255)
    receiver =models.CharField(max_length =255)
   

class invitation(models.Model):
    sender =models.CharField(max_length =255)
    receiver =models.CharField(max_length =255)
    status_choices = ('pending','pending'),('Accepted','Accepted')
    status = models.CharField(max_length=10, choices=status_choices, default='pending')
    invited_by = models.CharField(User,max_length=10, blank=True)


class userProfile(models.Model):
    user =models.CharField(max_length =255)
    courseId =models.CharField(max_length =255)
    chaptertitle =models.CharField(max_length =255)
    Description = models.CharField(max_length =255)