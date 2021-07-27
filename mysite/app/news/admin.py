from django.contrib import admin

from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','text')



admin.site.register(News, NewsAdmin)