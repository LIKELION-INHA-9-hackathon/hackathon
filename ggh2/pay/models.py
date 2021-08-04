from enum import unique
from goods.models import TimeStampModel
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from user.models import User
from goods.models import Goods
from cabinet.models import Cabinet_manage
#-*-coding:utf-8-*-

class Payment(TimeStampModel):
    goods_update_id=models.ForeignKey(Goods,on_delete=CASCADE,verbose_name="결제제품")
    pay_time = models.CharField(max_length=20) # 결제 소요 시간

class Delivery(models.Model):
    order_id = models.ForeignKey(Payment,on_delete=CASCADE,verbose_name="주문번호")
    location = models.ForeignKey(Cabinet_manage,on_delete=CASCADE,verbose_name="배송위치")
    due_date = models.CharField(max_length=8) # 배송예송 날짜