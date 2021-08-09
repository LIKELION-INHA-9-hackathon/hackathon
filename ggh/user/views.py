from django.shortcuts import render,redirect,get_object_or_404
from user.models import *
from cabinet.models import *
from goods.models import *
from wish.models import *
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .forms import *
from argon2 import PasswordHasher

# https://gosmcom.tistory.com/143?category=349443

def home(req):
    user_pk=req.session.get('user')

    if user_pk :  # session에 user_pk 정보가 있다면
        user = User.objects.get(pk=user_pk)
        return HttpResponse(user.nickname)
    return HttpResponse("로그인 성공") #없으면 home으로 


def check_password(checkpw,originalpw):
    if checkpw==originalpw:
        return True
    else:
        return False

# 로그인
def login(req):
    if req.method=="GET":
        return render(req,'login.html')
    elif req.method=="POST":
        nickname = req.POST.get('nickname')
        password = req.POST.get('password')

        res_data={}
        if not (nickname and password):
            res_data['error']="모든 칸을 다 입력해주세요"

        else:
            #기존(DB)에 있는 User 모델과 같은 값인 걸 가져온다.
            user = User.objects.get(nickname = nickname) #(필드명=값)

            #비밀번호가 맞는지 확인한다.
            if check_password(password,user.password):
                #응답 데이터 세션에 값 추가. 수신측 쿠키에 저징됨
                req.session['user'] = user.id 
                return redirect('/')
            else:
                res_data['error'] = "비밀번호가 틀렸습니다."
        return render(req,'login.html',res_data) #응답 데이터 res_data 전달


# 로그아웃 
def logout(req) : 
    if req.session['user']:
        del(req.session['user'])
    return redirect('/')


                                                                                   # 기본구현
#######################################################################################
                                                                                # user
                                                                                
# 회원가입
# user_create = register
# 기존대로 []하면 이름 까먹었는데 에러가 뜬다. 

def user_create(req):
        if req.method == 'POST':
            user_email = req.POST.get('user_email', None) 
            name = req.POST.get('name', None)
            nickname = req.POST.get('nickname', None)
            password = req.POST.get('password', None)
            re_password = req.POST.get('re_password', None)
            ph_no = req.POST.get('ph_no', None)
            birth = req.POST.get('birth', None)
            location = req.POST.get('location', None)
            cabinet = req.POST.get('cabinet', None)
            gender=req.POST.get('gender', None)
            marketing=req.POST.get('marketing', None)
    
            res_data ={}
    
            if not ( nickname and password and re_password) : 
                res_data['error'] = "모든 값을 입력하세요"
    
            elif password != re_password:
                res_data['error'] = "비밀번호가 다릅니다."
    
            else : 
                user = User (
                    nickname = nickname,
                    password = make_password(password),
                    user_email = user_email, 
                    name = name, 
                    ph_no= ph_no, 
                    birth = birth, 
                    location = location, 
                    cabinet = cabinet, 
                    marketing = marketing, 
                    gender = gender
                )
    
                user.save()
            return redirect('/')

        elif req.method =="GET":
            return render(req,'user/user_create.html')


# 프로필
#def user_read(req,id):
#    user = get_object_or_404(User,pk=id)
#    wish_list = Wish_list.objects.all().filter(user_id=id)
#    context = {
#        'data' : user,
#        'wish_list' : wish_list
#    }
#    return render(req,'user/user_read.html',context)

# 프로필 수정 
# def user_update(req):
#     user = get_object_or_404(User)
#     if req.method == "POST":
#         user.user_email = req.POST['user_email']
#         user.name = req.POST['name']
#         user.nickname = req.POST['nickname']
#         user.password = req.POST['password']
#         user.ph_no = req.POST['phone_number']
#         user.birth = req.POST['birthday']
#         user.location = req.POST['location']
#         user.cabinet = req.POST['cabinet']
#         user.save()
#         return redirect('/user/'+str(user.id))
#     return render(req,'user/user_update.html',{'data' : user})
# 
# # 회원탈퇴 
# def user_delete(req,id):
#     user = get_object_or_404(User,pk=id)
#     user.delete()
#     return redirect('/')
