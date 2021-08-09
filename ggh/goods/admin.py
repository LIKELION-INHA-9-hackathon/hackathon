from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin (admin.ModelAdmin):
    list_display=['name', 'slug']
    prepopulated_fields={'slug' : ('name',)}

admin.site.register (Category, CategoryAdmin)

class GoodsAdmin(admin.ModelAdmin):
    list_display=['name', 'sale_price', 'type', 'category', 'recruitment_no', 'expired', 'pre_people', 'uploader']
    list_filter = ['available_display', 'created','modified', 'category']
    prepopulated_fields={'slug' : ('name',)}

admin.site.register (Goods,GoodsAdmin)
