from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'password', 'ph_no', 'cabinet', 'location']

admin.site.register (User, UserAdmin)
