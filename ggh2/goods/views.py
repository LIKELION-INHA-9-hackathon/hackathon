from django.shortcuts import render,redirect,get_object_or_404
from user.models import *
from cabinet.models import *
from goods.models import *
from pay.models import *
from wish.models import *

def goods_create(req):
    user_pk = req.session.get('user')
    if not user_pk :
        return redirect('/login')
    elif user_pk:
        if req.method == 'POST':
            goods = Goods()
            goods_img=Goods_img()
            goods.name = req.POST['name']
            goods.price = int(req.POST['price'])
            goods.type = req.POST['type']
            goods.category = req.POST['category']
            goods.title = req.POST['title']
            goods.content = req.POST['content']
            goods.recruitment_no = int(req.POST['recruitment_no'])
            goods.expired = req.POST['expired']
            goods.pre_people = int(req.POST['pre_people'])
            user = User.objects.get(pk=user_pk)
            goods.uploader = user
            goods.save()
            goods_img.goods_id = goods
            goods_img.thumbnail = req.FILES['thumbnail']
            goods_img.otherimg = goods.thumbnail = req.FILES['image']
            goods_img.save()
            return redirect('/goods/'+str(goods.id))
    return render(req,'goods_create.html')

def goods_read_all(req):
    goods = Goods.objects.all()
    context = {
        'data' : goods
    }
    return render(req,'goods_read_all.html',context)

def goods_read_one(req,id):
    goods = get_object_or_404(Goods,pk=id)
    context = {
        'data' : goods
    }
    user_pk = req.session.get('user')
    if not user_pk :
        return redirect('/login')
    elif user_pk:
        if req.method == 'POST':
            pay = Payment()
            pay.user_id = User.objects.get(pk=user_pk)
            pay.goods_update_id = goods
            pay.quantity = req.POST['quantity']
            pay.save()
    return render(req,'goods_read.html',context)

def goods_update(req,id):
    goods=get_object_or_404(Goods,pk=id)
    if req.method == 'POST':
        goods.name = req.POST['name']
        goods.price = int(req.POST['price'])
        goods.type = req.POST['type']
        goods.category = req.POST['category']
        goods.title = req.POST['title']
        goods.content = req.POST['content']
        goods.recruitment_no = int(req.POST['recruitment_no'])
        goods.expired = req.POST['expired']
        goods.pre_people = goods.pre_people + 1
        goods.save()
        return redirect('/goods/'+str(goods.id))
    return render(req,'goods_update.html',{'data':goods})

def goods_delete(req,id):
    goods = get_object_or_404(Goods,pk=id)
    goods.delete()
    return redirect('/goods/')

                                                                                # user