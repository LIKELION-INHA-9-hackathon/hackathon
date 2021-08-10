from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
# Create your models here.
#-*-coding:utf-8-*-

class User(models.Model):
    # pk : django 자동으로 제공하는 id 값으로 할거임
    user_email = models.CharField(max_length=200,default='dydrkfsla0821@gmail.com')
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    ph_no = models.CharField(max_length=11)
    birth = models.CharField(max_length=9)
    location = models.CharField(max_length=100)
    cabinet = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "user",null=True)
    