from django.urls import path
from .views import * 

app_name = 'user'

urlpatterns = [
    path('login/', login,name = 'login'),
    path('register/', user_create, name = 'user_create'),
    path('logout/',logout, name = 'logout'), 
    path('home/',home)
] 
