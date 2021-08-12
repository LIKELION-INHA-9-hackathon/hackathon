from django.contrib import admin
from .models import *
# Register your models here.

class Goods_imgInline(admin.TabularInline) : 
    model = Goods_img    

class GoodsAdmin(admin.ModelAdmin):
    inlines = [Goods_imgInline, ]


admin.site.register(Goods, GoodsAdmin)

class CategoryAdmin (admin.ModelAdmin):
    list_display=['name']


admin.site.register(Category, CategoryAdmin)
