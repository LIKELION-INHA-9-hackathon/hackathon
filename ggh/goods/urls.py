"""ggh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import * 

app_name = 'goods'


urlpatterns = [
    path('new/',goods_create,name="goods_create"),
    path('',goods_read_all,name="goods_read_all"),
    path('<int:id>/',goods_read_one,name="goods_read_one"),
    path('update/<int:id>/',goods_update,name="goods_update"),
    path('delete/<int:id>/',goods_delete,name="goods_delete"),
]
