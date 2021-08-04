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
from django.contrib import admin
from django.urls import path
from user import views as user
from goods import views as goods
from cabinet import views as cabinet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user.home,name="home"),
    path('login/',user.login,name="login"),

    path('user/new',user.user_create,name="user_create"),
    path('user/<int:id>',user.user_read,name="user_read"),
    path('user/update/<int:id>',user.user_update,name="user_update"),
    path('user/delete/<int:id>',user.user_delete,name="user_delete"),

    path('goods/new',goods.goods_create,name="goods_create"),
    path('goods/',goods.goods_read_all,name="goods_read_all"),
    path('goods/<int:id>',goods.goods_read_one,name="goods_read_one"),
    path('goods/update/<int:id>',goods.goods_update,name="goods_update"),
    path('goods/delete/<int:id>',goods.goods_delete,name="goods_delete"),

    path('cabinet/',cabinet.cabinet_read_all,name="cabinet_read_all"),
    path('cabinet/<int:id>',cabinet.cabinet_read_one,name="cabinet_read_one"),
    path('cabinet/update/<int:id>',cabinet.cabinet_update,name="cabinet_update"),
    path('cabinet/delete/<int:id>',cabinet.cabinet_delete,name="cabinet_delete"),
]
