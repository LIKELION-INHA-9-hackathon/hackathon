from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import logout as auth_logout
from user.models import *
from cabinet.models import *
from goods.models import *
from pay.models import *
from wish.models import *

def home(req):
    # if req.method=="POST":
    #     searchtext = req.POST['searchtext']
    #     location = req.POST['location']
    #     cabinet = req.POST['cabinet']
    user_pk = req.session.get('user')
    context = {
        'user_pk' : user_pk,
    }
    return render(req, 'home.html',context)

# def search(req):
#     if req.method == "POST":
#         searchtext = req.POST['searchtext']
#         cabinet=Cabinet_manage.objects.filter(location_contains=searchtext)
#         goods=Goods.objects.filter(name_contaions=searchtext)
#         user=User.objects.filter(nickname=searchtext)
#         if not cabinet :




def check_password(checkpw,originalpw):
    if checkpw==originalpw:
        return True
    else:
        return False

def login(req):
    if req.method=="GET":
        return render(req,'login.html')
    elif req.method=="POST":
        user_id = req.POST.get('user_id')
        user_pw = req.POST.get('user_pw')

        res_data={}
        if not (user_id and user_pw):
            res_data['error']="모든 칸을 다 입력해주세요"

        else:
            #기존(DB)에 있는 Fuser 모델과 같은 값인 걸 가져온다.
            user = User.objects.get(user_email = user_id) #(필드명=값)

            #비밀번호가 맞는지 확인한다.
            if check_password(user_pw,user.password):
                #응답 데이터 세션에 값 추가. 수신측 쿠키에 저징됨
                req.session['user'] = user.id 
                return redirect('/')
            else:
                res_data['error'] = "비밀번호가 틀렸습니다."
                return redirect('/login/')
        return render(req,'login.html',res_data) #응답 데이터 res_data 전달

def logout(req):
    auth_logout(req)
    return redirect('/')

                                                                                   # 기본구현
######################################################################################
                                                                                # user

def user_create(req):
    if req.method == 'POST':
        user = User()
        user.user_email = req.POST['user_email']
        user.name = req.POST['name']
        user.nickname = req.POST['nickname']
        user.password = req.POST['password']
        user.ph_no = req.POST['phone_number']
        year = req.POST['year']
        month = req.POST['month']
        day = req.POST['day']
        user.birth=str(year)+str(month)+str(day)
        user.location = req.POST['location']
        user.cabinet = req.POST['cabinet']
        user.image = req.FILES['images']
        user.save()
        return redirect('/user/'+str(user.id))
    return render(req,'user/user_create.html')

def user_read(req,id):
    user = get_object_or_404(User,pk=id)
    wish_list = Wish_list.objects.all().filter(user_id=id)
    context = {
        'data' : user,
        'wish_list' : wish_list
    }
    return render(req,'user/user_read.html',context)

def user_update(req,id):
    user = get_object_or_404(User, pk=id)
    if req.method == "POST":
        user.user_email = req.POST['user_email']
        user.name = req.POST['name']
        user.nickname = req.POST['nickname']
        user.password = req.POST['password']
        user.ph_no = req.POST['phone_number']
        user.birth = req.POST['birthday']
        user.location = req.POST['location']
        user.cabinet = req.POST['cabinet']
        user.image = req.FILES['images']
        user.save()
        return redirect('/user/'+str(user.id))
    return render(req,'user/user_update.html',{'data' : user})

def user_delete(req,id):
    user = get_object_or_404(User,pk=id)
    user.delete()
    return redirect('/')

                                                                                # user