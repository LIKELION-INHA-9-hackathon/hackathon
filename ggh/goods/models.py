from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator

from user.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True) # db_index : 해당 필드에 대해서 Database index 생성
    meta_description = models.TextField(blank=True) # 구글 등 검색엔진에서 검색 정보 제공 
    slug = models.SlugField(max_length=200, db_index=True, unique =True, allow_unicode=True) # 데이터로 url 만드는 필드 #https://itmining.tistory.com/119

    class Meta : 
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name



class Goods(models.Model):
    fresh_or_not=(
        ('냉장','냉장상품'),
        ('냉동','냉동식품'),
        ('그외','그 외 모두')
    )
    name = models.CharField(max_length=200, db_index=True) # 물품명 
    slug=models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True) # slug

    sale_price=models.DecimalField(max_digits=10, decimal_places=2) # 공구 가격
    norm_price = models.DecimalField(max_digits=10, decimal_places=2) # 정상 가격

    type = models.CharField(choices=fresh_or_not, max_length=5) # 매물 종류(냉장식품인지 냉동식품인지 그 외의 물건인지
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    tags = models.CharField(max_length=200) # 조금 더 상세한 내용을 적을 수 있도록 ex) 냉동 도시락, 과자, 비누... (해시태그로 하면 좋을 것 같다.)
    title = models.CharField(max_length=100) # 게시글 제목
    content = models.TextField() # 게시글 내용 

    recruitment_no = models.PositiveBigIntegerField(validators=[MaxValueValidator(10)]) #모집인원
    expired = models.CharField(max_length=8)
    pre_people = models.PositiveBigIntegerField(validators=[MaxValueValidator(10)] ,blank=True, null = True) #이미 공구에 참여한 사람

    uploader = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="작성자")

    created = models.DateTimeField(auto_now_add=True) # 작성 시간
    modified = models.DateTimeField(auto_now=True) # 수정 시간
    deadline = models.CharField(max_length=200) # 마감 날짜

    image=models.ImageField(upload_to='goods/%Y/%m/%d', blank=True) # 이미지
    url=models.URLField(null = True, blank=True) # 공구시 참고 url (url 올리면 자동으로 썸네일처럼 생기면 좋을 것 같다.)

    available_display = models.BooleanField('Display', default = True) # 공구 완료 시 상품 노출 여부 
    available_order = models.BooleanField('Order', default=True) # 인원이 다치면 주문 불가하도록

    hits = models.PositiveIntegerField(default=0) # 인기(조회수)

    class Meta:
        ordering=['-modified', '-created'] # 최신 순으로