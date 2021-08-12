from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
# Create your models here.
#-*-coding:utf-8-*-

class User(models.Model):
    Gender_Choices =(
        ('Male','남자'),
        ('Female','여자'),
        ('None','선택안함')

    )
    # pk : django 자동으로 제공하는 id 값으로 할거임
    user_email = models.CharField(max_length=200, default='dydrkfsla0821@gmail.com')
    name = models.CharField(max_length=10, default = '')
    nickname = models.CharField(max_length=20, default = '')
    password = models.CharField(max_length=30, default = '')
    ph_no = models.CharField(max_length=11, default = '')
    birth = models.CharField(max_length=9, default = '')
    location = models.CharField(max_length=100, default = '')
    cabinet = models.CharField(max_length=100, default = '')
    image = models.ImageField(upload_to = "user",null=True,blank=True, default='../static/img/default_img.jpg')
    gender=models.CharField(max_length=10, choices=Gender_Choices, default='')

    def __str__(self):
        return self.user_email

    