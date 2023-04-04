from django.db import models
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
    date = models.DateField()   ``
   

class invitation(models.Model):
    sender =models.CharField(max_length =255)
    receiver =models.CharField(max_length =255)
    message =models.CharField(max_length =255)
    accept = models.CharField(max_length =255)
    timestamp = models.DateTimeField(auto_now_add=True)


class userProfile(models.Model):
    user =models.CharField(max_length =255)
    courseId =models.CharField(max_length =255)
    chaptertitle =models.CharField(max_length =255)
    Description = models.CharField(max_length =255)