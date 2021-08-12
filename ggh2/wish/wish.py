from decimal import Decimal
from django.conf import settings
from goods.models import *


class Wish(object):
    def __init__(self, request):
        self.session = request.session
        wish = self.session.get(settings.WISH_ID)
        if not wish:
            wish = self.session[settings.WISH_ID] = {}
        self.wish = wish

    def __iter__(self):
        wish_ids = self.wish.keys()

        goods = Goods.objects.filter(id__in=wish_ids)

        for goods in goods:
            self.wish[str(goods.id)]['goods'] = goods


    def add(self, goods, quantity=1, is_update=False):
        goods_id = str(goods.id)
        if goods_id not in self.wish:
            self.wish[goods_id] = {'quantity':0, 'price':str(goods.price)}

        if is_update:
            self.wish[goods_id]['quantity'] = quantity
        else:
            self.wish[goods_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.WISH_ID] = self.wish
        self.session.modified = True

    def remove(self, goods):
        goods_id = str(goods.id)
        if goods_id in self.wish:
            del(self.cart[goods_id])
            self.save()

    def clear(self):
        self.session[settings.WISH_ID] = {}
        self.session['coupon_id'] = None
        self.session.modified = True


    def get_product_total(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.wish.values())

