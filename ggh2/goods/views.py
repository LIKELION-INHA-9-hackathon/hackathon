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
            goods.name = req.POST.get('name')#
            goods.price = int(req.POST.get('price'))#
            goods.type = req.POST.get('type')#
            category = req.POST.get('category')
            goods.category = Category.objects.get(pk=category)
            goods.title = req.POST.get('title')#
            goods.content = req.POST.get('content')#
            goods.recruitment_no = int(req.POST.get('recruitment_no'))#
            goods.expired = req.POST.get('expired')#
            goods.pre_people = 1
            goods.ori_price = int(req.POST.get('ori_price')) #
            goods.due_date = req.POST.get('due_date')#
            cabinet = req.POST.get('cabinet')
            goods.cabinet = Cabinet_manage.objects.get(location=cabinet)
            goods.description = req.POST.get('description')#
            goods.thumbnail = req.FILES.get('thumbnail')#
            user = User.objects.get(pk=user_pk)
            goods.uploader = user#
            goods.save()
            goods_img.goods_id = goods
            goods_img.otherimg = req.FILES.get('image')
            goods_img.save()
            return redirect('/goods/'+str(goods.id))
    context={
        'user_pk' : user_pk,
    }
    return render(req,'goods_create.html',context)

def goods_popup(req):
    return render(req,'popup.html')
    

def goods_read_all(req):
    sort_text = req.GET.get('sort')
    if sort_text == 'fast':
        goods = Goods.objects.order_by('expired')
    elif sort_text == 'slow':
        goods = Goods.objects.order_by('-expired')
    elif sort_text == 'low':
        goods = Goods.objects.order_by('price')
    elif sort_text == 'high':
        goods = Goods.objects.order_by('-price')
    else :
        goods = Goods.objects.order_by('-created')
    user_pk = req.session.get('user')
    goods1=[] 
    goods2=[]
    i=0
    for g in goods:
        if i < 3:
            goods1.append(g)
        elif i < 6 :
            goods2.append(g)
        else :
            break
        i+=1

    context = {
        'user_pk' : user_pk,
        'goods1' : goods1,
        'goods2' : goods2,
    }
    return render(req,'goods_read_all.html',context)

def goods_read_beauty(req):
    sort_text = req.GET.get('sort')
    if sort_text == 'fast':
        goods = Goods.objects.filter(category=10).order_by('expired')
    elif sort_text == 'slow':
        goods = Goods.objects.filter(category=10).order_by('-expired')
    elif sort_text == 'low':
        goods = Goods.objects.filter(category=10).order_by('price')
    elif sort_text == 'high':
        goods = Goods.objects.filter(category=10).order_by('-price')
    else :
        goods = Goods.objects.filter(category=10).order_by('-created')
    user_pk = req.session.get('user')
    goods1=[] 
    goods2=[]
    i=0
    for g in goods:
        if i < 3:
            goods1.append(g)
        elif i < 6 :
            goods2.append(g)
        else :
            break
        i+=1

    context = {
        'user_pk' : user_pk,
        'goods1' : goods1,
        'goods2' : goods2,
    }
    return render(req,'goods_read_beauty.html',context)

def goods_read_food(req):
    sort_text = req.GET.get('sort')
    if sort_text == 'fast':
        goods = Goods.objects.filter(category=9).order_by('expired')
    elif sort_text == 'slow':
        goods = Goods.objects.filter(category=9).order_by('-expired')
    elif sort_text == 'low':
        goods = Goods.objects.filter(category=9).order_by('price')
    elif sort_text == 'high':
        goods = Goods.objects.filter(category=9).order_by('-price')
    else :
        goods = Goods.objects.filter(category=9).order_by('-created')
    user_pk = req.session.get('user')
    goods1=[] 
    goods2=[]
    i=0
    for g in goods:
        if i < 3:
            goods1.append(g)
        elif i < 6 :
            goods2.append(g)
        else :
            break
        i+=1

    context = {
        'user_pk' : user_pk,
        'goods1' : goods1,
        'goods2' : goods2,
    }
    return render(req,'goods_read_food.html',context)

def goods_read_one(req,id):
    
    goods = get_object_or_404(Goods,pk=id)
    goods_img = Goods_img.objects.filter(goods_id=goods)
    comments = goods.goods_comment.all()
    user=User.objects.get(pk=goods.uploader.id)
    context = {
        'goods' : goods,
        'photo' : goods_img,
        'comment' : comments,
        'user' : user,
    }
 
    user_pk = req.session.get('user')
    if not user_pk : # ????????? ??????
        return redirect('/login')
    elif user_pk: # ????????? ???
        if req.method == 'POST':
            pay = Payment()
            pay.user_id = User.objects.get(pk=user_pk)
            pay.goods_update_id = goods
            pay.quantity = 1
            pay.save()
    return render(req,'goods_read_one.html',context)

def goods_update(req,id):
    goods=get_object_or_404(Goods,pk=id)
    goods_img=Goods_img()
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
        goods.ori_price = req.POST['ori_price']
        goods.description=req.POST['description']
        goods.description=req.POST['cabinet']
        goods.due_date = req.POST['due_date']
        goods.thumbnail = req.POST['thumbnail']
        goods.save()
        for img in req.FILE.getlist('imgs') :
            photo = Goods_img()
            photo.goods_id=goods
            photo.otherimg=img
            photo.save()
            goods_img.goods_id = goods
        return redirect('/goods/'+str(goods.id))
    return render(req,'goods_update.html',{'data':goods})

def goods_delete(req,id):
    goods = get_object_or_404(Goods,pk=id)
    goods.delete()
    return redirect('/goods/')


def goods_comment_create(req, id): 
    user_pk = req.session.get('user')
    if not user_pk:
        return redirect('/login')
    elif user_pk:
        if req.method == 'POST':
            goods = get_object_or_404(Goods, pk = id) 
            user=User.objects.get(pk=user_pk)
            goods.goods_comment.create(content=req.POST['comment'],user_id=user,goods_id=goods)
            return redirect('/goods/'+str(goods.id))
    return render(req,'goods_read_one.html')
