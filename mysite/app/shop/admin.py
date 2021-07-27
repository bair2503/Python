from django.contrib import admin

from .models import *


class CategoryShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ProductShopAdmin(admin.ModelAdmin):
    list_display  = ("id", 'name', 'category', 'prace')




admin.site.register(CategoryShop, CategoryShopAdmin)
admin.site.register(ProductShop, ProductShopAdmin)