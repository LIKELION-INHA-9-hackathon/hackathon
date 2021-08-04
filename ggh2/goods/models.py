from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField
from user.models import User
#-*-coding:utf-8-*-

class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Goods(TimeStampModel):
    fresh_or_not=(
        ('냉장','냉장상품'),
        ('냉동','냉동식품'),
        ('그외','그 외 모두')
    )
    name = models.CharField(max_length=10)
    price = models.IntegerField(max_length=50)
    type = models.CharField(choices=fresh_or_not, max_length=5) #냉장식품인지 냉동식품인지 그 외의 물건인지
    category = models.CharField(max_length=50) # 조금 더 상세한 내용을 적을 수 있도록 ex) 냉동 도시락, 과자, 비누...
    title = models.CharField(max_length=100)
    content = models.TextField()
    recruitment_no = models.IntegerField(max_length=10) #모집인원
    expired = models.CharField(max_length=8)
    pre_people = models.IntegerField(max_length=10) #이미 공구에 참여한 사람
    uploader = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="작성자")
