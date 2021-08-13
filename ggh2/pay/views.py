from django.shortcuts import render, redirect, get_object_or_404
import requests
from requests.api import get
from user.models import *
from goods.models import *
from pay.models import *
import qrcode
# Create your views here.

#  결제 물건 확인 
def kakaoPay(request,goods_id):
    user_pk = request.session.get('user')
    if not user_pk :
        return redirect('/login')
    elif user_pk:
        user = User.objects.get(pk=user_pk)
        goods = Goods.objects.get(pk=goods_id)
        pay = Payment.objects.filter(goods_update_id=goods_id).order_by('-created')
        payment = pay[0]
        context={
            'user' : user,
            'goods' : goods,
            'payment' : payment,
        }
        request.session['goods']=goods_id
        request.session['payment']=payment.id
    return render(request, 'kakaopay.html',context)


# 결제 버튼 누르고 나타나는 
def kakaoPayLogic(request):
    user_id = request.session.get('user')
    goods_id = request.session.get('goods')
    payment_id = request.session.get('payment')
    user=User.objects.get(pk=user_id)
    goods=Goods.objects.get(pk=goods_id)
    payment=Payment.objects.get(pk=payment_id)
        
    URL = 'https://kapi.kakao.com/v1/payment/ready'
    admin_key = '8586b731d8d6f04ce7ef1f424049eb7e'
    headers = {

        "Authorization" : f"KakaoAK {admin_key}",   # 변경불가
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8", # 변경불가
    }
    params = {
        "cid": "TC0ONETIME",    # 테스트용 CID값
        "partner_order_id": "{}".format(payment.id),     # 주문번호
        "partner_user_id":"{}".format(user.id),    # 유저 아이디
        "item_name": "{}".format(goods.name),        # 구매 물품 이름
        "quantity": "{}".format(payment.quantity),                # 구매 물품 수량
        "total_amount": "{}".format(goods.price),        # 구매 물품 가격
        "tax_free_amount": "0",         # 구매 물품 비과세 
        'approval_url':'http://127.0.0.1:8000/pay/paySuccess', 
        'fail_url':'http://127.0.0.1:8000/pay/payFail',
        'cancel_url':'http://127.0.0.1:8000/pay/payCancel',
    }

    res = requests.post(URL, headers=headers, params=params)
    result = res.json()
    request.session['order_id'] = "{}".format(user.id)
    request.session['user_id'] = "{}".format(user.id)
    request.session['tid'] = result['tid'] # 결제 승인시 사용할 tid를 세션에 저장
    return redirect(result['next_redirect_pc_url']) # 결제 페이지로 넘어갈 url을 저장

# 결제 성공창 
def paySuccess(request): 
    URL = "https://kapi.kakao.com/v1/payment/approve"
    headers = {
    "Host" : "kapi.kakao.com",
    "Authorization" : "KakaoAK " + "8586b731d8d6f04ce7ef1f424049eb7e",   # 변경불가
    }
    params = {
        'cid':'TC0ONETIME',
        'tid': request.session['tid'],
        'partner_order_id':'partner_order_id',
        'partner_user_id':'partner_user_id',
        'pg_token': request.GET['pg_token']
    }
    res = requests.post(URL, headers=headers, params=params)
    result = res.json()
    if result.get('msg'):
        return redirect('/pay/payFail')
    else:
        barcode = Barcode()
        payment_id=request.session.get('payment')
        barcode.order_id = payment_id
        img =qrcode.make(barcode.order_id)
        img.save("../barcode/"+str(barcode.order_id)+".png")
        barcode.barcode = img
        barcode.save()
        return render(request, 'paySuccess.html')

def payFail(request):
    return render(request, 'payFail.html')


def payCancel(request):
    return render(request, 'payCancel.html')