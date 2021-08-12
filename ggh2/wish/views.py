from enum import unique

from django.core.exceptions import ObjectDoesNotExist
from wish.models import *

from django.shortcuts import get_object_or_404, redirect
from goods.models import TimeStampModel
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField
from user.models import User
from goods.models import Goods

def wish_id(req):
    wish = req.session.session_key
    if not wish : 
        wish = req.session.create()
    return wish

def add_wish(req, product_id):
    product = Goods.objects.get(id = product_id)
    try : 
        wish = Wish_list.objects.get(wish_id=wish_id(req))
    except Wish_list.DoesNotExist : 
        wish = Wish_list.create(
            wish_id = wish_id(req)
        )
        wish.save()

    try : 
        wish_item=Wish_item.objects.get(product=product, wish=wish)
        wish_item.quantity += 1
        wish_item.save()
    except Wish_item.DoesNotExist:
        wish_item = Wish_item.objects.create(
            product=product,
            quantity=1,
            wish=wish
        )
        wish_item.save()
    return redirect('user_read')

def wish_detail(req, total=0, counter=0, wish_item=None):
    try : 
        wish = Wish_list.objects.get(wish_id=wish_id(req))
        wish_items = Wish_item.objects.filter(wish=wish, active=True)

        for wish_item in wish_items : 
            total += (wish_item.product.price* wish_item.quantity)
            counter += wish_item.quantity
    except ObjectDoesNotExist:
        pass
    
    return render (req, 'user_read', dict(wish_items=wish_items, total=total, counter=counter))