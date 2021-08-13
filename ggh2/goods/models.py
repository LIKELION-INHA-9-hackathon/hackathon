from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField
from user.models import User
from cabinet.models import *
#-*-coding:utf-8-*-

class Category(models.Model):
    name=models.CharField(max_length=200)
class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Goods(TimeStampModel):
    fresh_or_not=(
        ('냉장','냉장상품'),
        ('냉동','냉동식품'),
        ('그외','그 외 모두')
    )
    name = models.CharField(max_length=200)
    price = models.IntegerField()#공구가
    type = models.CharField(choices=fresh_or_not, max_length=10) #냉장식품인지 냉동식품인지 그 외의 물건인지
    category = models.ForeignKey(Category,on_delete = CASCADE,max_length=100) # 조금 더 상세한 내용을 적을 수 있도록 ex) 냉동 도시락, 과자, 비누...
    title = models.CharField(max_length=100)
    content = models.TextField()
    recruitment_no = models.IntegerField() #모집인원
    expired = models.CharField(max_length=9)
    pre_people = models.IntegerField(default=0) #이미 공구에 참여한 사람
    uploader = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="작성자")
    ori_price = models.IntegerField() #원가
    description = models.TextField()
    cabinet = models.ForeignKey(Cabinet_manage,on_delete=CASCADE,verbose_name="배송지")
    due_date = models.CharField(max_length=8) # 배송예송 날짜
    thumbnail = models.ImageField(upload_to="thumbnail",null=True,blank=True)

    def __str__(self):
        return self.name



class Goods_img(models.Model):
    goods_id = models.ForeignKey(Goods,on_delete=CASCADE)
    otherimg = models.ImageField(upload_to="goods",null=True,blank=True)

