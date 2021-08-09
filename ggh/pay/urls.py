from django.urls import path
from .views import * 

app_name = "pay"

urlpatterns = [
    path('<int:id>/', kakaoPay, name = "kakao"),
    path('kakaoPayLogic/', kakaoPayLogic, name = "kakaopay"),
    path('paySuccess/', paySuccess),
    path('payFail/', payFail),
    path('payCancel/', payCancel),
]
