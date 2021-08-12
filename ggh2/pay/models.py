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
    user_id = models.ForeignKey(User,on_delete=CASCADE,verbose_name="주문자")
    quantity = models.IntegerField(verbose_name="주문수량")

class Barcode(TimeStampModel):
    order_id = models.ForeignKey(Payment,on_delete=CASCADE)
    user_id = models.ForeignKey(User,on_delete=CASCADE)
    order_barcode = models.ImageField(upload_to="")
