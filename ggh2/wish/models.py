from enum import unique
from goods.models import TimeStampModel
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField
from user.models import User
from goods.models import Goods
#-*-coding:utf-8-*-

class Wish_list(TimeStampModel): #찜
    user_id = models.ForeignKey(User,on_delete=CASCADE,verbose_name="찜한사람")
    goods_id = models.ForeignKey(Goods,on_delete=CASCADE,verbose_name="찜한물품")

class Wish_item(TimeStampModel) : 
    product =models.ForeignKey(Goods, on_delete=models.CASCADE)
    wish = models.ForeignKey(Wish_list, on_delete=models.CASCADE)
    #quantity = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta : 
        db_table = 'WishItem'
    
    def __str__(self):
        return self.product


class Participant(TimeStampModel): #공구 참여
    complete_or_not=(
        (1,'공구완료'),
        (2,'공구진행'),
        (3,'완료임박')
    )
    user_id = models.ForeignKey(User,on_delete=CASCADE,verbose_name="공구참여사람")
    goods_id = models.ForeignKey(Goods,on_delete=CASCADE,verbose_name="공구물품")
    complete = models.IntegerField(choices=complete_or_not)