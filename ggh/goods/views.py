from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.

from .models import * 
from user.models import *
from goods.forms import * 

# Read
def goods_read_all(req):
    goods = Goods.objects.all()
    context = {
        'data' : goods
    }
    return render(req,'goods/read_all.html',context)

# 로그인했을때만 결제할 수 있게 해야 한다. 
def goods_read_one(req,id):
    goods = get_object_or_404(Goods, pk=id)
    return render(req, 'goods/read.html', {'data' : goods})


#  req.session['user'] = user.id 

# Create
def goods_create(req):
    user_session = req.session.get('user_session', '')
    context = {'user_session' : user_session}

    if req.method == 'GET' : 
        create_form = CreateForm()
        return render (req, 'goods/create.html', create_form)

    elif req.method == 'POST' : 
        create_form = CreateForm(req.POST)

        if create_form.is_valid():
            uploaders= User.objects.get(user_id = user_session)
            
            create = Goods(
                name = create_form.name,
                sale_price = create_form.sale_price,
                norm_price = create_form.norm_price,
                type = create_form.type,
                category = create_form.category,
                tags=create_form.tags,
                title = create_form.title,
                content = create_form.content,
                recruitment_no = create_form.recruitment_no,
                deadline = create_form.deadline,
                image=create_form.image,
                url=create_form.url,
                uploader = uploaders
            )
            create.save()
            

            return redirect('/') 

        else : 
            context['forms'] = create_form 
            if create_form.errors :
                for value in create_form.errors.values():
                    context['error'] = value
            return render(req, 'goods/create.html', context)


# Update
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
        goods.image=req.POST['image']
        goods.url=req.POST['url']
        goods.save()
        return redirect('/goods/'+str(goods.id))
    return render(req,'goods/update.html',{'data':goods})

# delete
def goods_delete(req,id):
    goods = get_object_or_404(Goods,pk=id)
    goods.delete()
    return redirect('/goods/')


def list(req):
    user_session = req.session.get('user_session', '')
    context = {'user_session' : user_session }

    return render(req, 'goods/read_all.html', context)