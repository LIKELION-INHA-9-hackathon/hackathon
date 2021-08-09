from django.shortcuts import render, redirect, get_object_or_404
import requests
from requests.api import get
from user.models import *
from goods.models import *
# Create your views here.

#  결제 물건 확인 
def kakaoPay(request):
    return render(request, 'kakaopay.html')


# 결제 버튼 누르고 나타나는 
def kakaoPayLogic(request, id):
    user=request.user
    goods=get_object_or_404(Goods,pk=id)


    if request.method =="POST" : 
        
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        admin_key = '8586b731d8d6f04ce7ef1f424049eb7e'
        headers = {

            "Authorization" : f"KakaoAK {admin_key}",   # 변경불가
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8", # 변경불가
        }
        params = {
            "cid": "TC0ONETIME",    # 테스트용 CID값
            "partner_order_id": "{}".format(user.id),     # 주문번호
            "partner_user_id": "{}".format(user.id),    # 유저 아이디
            "item_name": "{}".format(goods.name),        # 구매 물품 이름
            "quantity": "{}".format(goods.recruitment_no),                # 구매 물품 수량
            "total_amount": "{}".format(goods.sale_price),        # 구매 물품 가격
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
        'partner_order_id':request.session['order_id'] ,
        'partner_user_id':request.session['order_id'],
        'pg_token': request.GET['pg_token']
    }
    res = requests.post(URL, headers=headers, params=params)
    result = res.json()
    if result.get('msg'):
        return redirect('/pay/payFail')
    else:
        return render(request, 'paySuccess.html')

def payFail(request):
    return render(request, 'payFail.html')


def payCancel(request):
    return render(request, 'payCancel.html')
