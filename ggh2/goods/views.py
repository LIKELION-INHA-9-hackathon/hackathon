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
    context={
        'user_pk' : user_pk,
    }
    return render(req,'goods_create.html',context)

def goods_popup(req):
    return render(req,'popup.html')
    


def goods_read_one(req,id):
    goods = get_object_or_404(Goods,pk=id)
    goods_img = Goods_img.objects.all()
    comments = goods.goods_comment.all()
    context = {
        'data' : goods,
        'photo' : goods_img,
        'comment' : comments,
    }

    user_pk = req.session.get('user')
    if not user_pk : # 로그인 안함
        return redirect('/login')
    elif user_pk: # 로그인 함
        if req.method == 'POST':
            pay = Payment()
            pay.user_id = User.objects.get(pk=user_pk)
            pay.goods_update_id = goods
            pay.quantity = req.POST['quantity']
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

#def content_read(req,id):
#    goods=get_object_or_404(Goods,id)
    


# def participant(req,id):
#     goods=Goods.objects.all()
#     if goods.recruitmentno 
#                                                                                 # user

### 댓글 구현 

# class Comments(TimeStampModel):
#     user_id = models.ForeignKey(User, on_delete=CASCADE, verbose_name="작성자")
#     goods_id(blog) = models.ForeignKey(Goods, on_delete=CASCADE, verbose_name = "공구 참여 물품")
#     content(body) = models.TextField()



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


def goods_read_all(req) :
    if req.POST['category'] == 'all' : 
        goods =Goods.objects.all()
    
    elif req.POST['category'] =='decoration' :  # 데코/조명
        goods = Goods.objects.filter(category ='decoration')
    
    elif req.POST['category'] =='catndog' : # 패브릭/ 생활
        goods = Goods.objects.filter(category ='catndog')

    elif req.POST['category'] =='catndog' : # 키친
        goods = Goods.objects.filter(category ='catndog')
    
    elif req.POST['category'] =='catndog' : # 캠핑/트래블
        goods = Goods.objects.filter(category ='catndog')

    elif req.POST['category'] =='fabric' : # 디자인가전
        goods = Goods.objects.filter(category ='fabric')
    
    elif req.POST['category'] =='furniture_acceptance' :  # 가구/수납
        goods = Goods.objects.filter(category ='furniture_acceptance')

    elif req.POST['category'] =='food' :  # 푸드 
        goods = Goods.objects.filter(category ='food')
    
    elif req.POST['category'] =='beauty' :  # 뷰티
        goods = Goods.objects.filter(category ='beauty')

    elif req.POST['category'] =='catndog' : # 캣앤독
        goods = Goods.objects.filter(category ='catndog')
    
    elif req.POST['category'] =='toy' :  # 토이
        goods = Goods.objects.filter(category ='toy')

    elif req.POST['category'] =='baby' :  # 베이비/키즈
        goods = Goods.objects.filter(category ='baby')
    context ={
        'goods' : goods,
    }
    return render(req,'goods_read_all.html',context)
