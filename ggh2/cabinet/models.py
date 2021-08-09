from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from user.models import User
#-*-coding:utf-8-*-

class Cabinet_manage(models.Model):
    location = models.CharField(max_length=100)
    location_id = models.IntegerField() # 각 위치에 있는 cabinet의 id

class Cabinet_1(models.Model):
    location_id = models.ForeignKey(Cabinet_manage,on_delete=models.CASCADE,verbose_name="각각캐비넷")
    can_id = models.IntegerField()
    in_use = models.BooleanField()
    weight = models.IntegerField()

class Cabinet_2(models.Model):
    location_id = models.ForeignKey(Cabinet_manage,on_delete=models.CASCADE,verbose_name="각각캐비넷")
    can_id = models.IntegerField()
    in_use = models.BooleanField()
    weight = models.IntegerField()

class Cabinet_3(models.Model):
    location_id = models.ForeignKey(Cabinet_manage,on_delete=models.CASCADE,verbose_name="각각캐비넷")
    can_id = models.IntegerField()
    in_use = models.BooleanField()
    weight = models.IntegerField()