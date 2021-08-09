from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
#-*-coding:utf-8-*-


class User(models.Model):
    # pk : django 자동으로 제공하는 id 값으로 할거임
    cabinet_or_not=(
        ('인하대역', '인하대역'),
        ('신촌역', '신촌역'),
        ('회기역', '회기역')
    )
    gender_or_not=(
        ('남자', '남자'),
        ('여자', '여자'),
        ('선택안함','선택안함')
    )

    user_email = models.EmailField(max_length=200) # 이메일 (길이가 짧아서 200으로 바꿈)
    name = models.CharField(max_length=10) # 사용자 이름 
    nickname = models.CharField(max_length=20) # 사용자 아이디
    password = models.CharField(max_length=30) # 비밀번호
    ph_no = models.CharField(max_length=11) # 전화번호
    birth = models.CharField(max_length=9) # 생일 

    location = models.CharField(max_length=200) # 주소 
    cabinet = models.CharField(choices=cabinet_or_not,max_length=5) # 가까운 사물함
    image = models.ImageField(blank=True, null = True) # 프로필 이미지

    gender = models.CharField(choices=gender_or_not,max_length=5) # t성별 
    marketing = models.BooleanField() # 마케팅 수신 동의 

    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null =True, blank = True) # 신뢰도 

    def __str__(self) : 
        return self.name
