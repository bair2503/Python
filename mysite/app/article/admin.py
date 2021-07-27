from django.contrib import admin

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'prace', 'descripshion', 'viziboll', 'number')

class ArticleAdmin(admin.ModelAdmin):
    list_display  = ("id", 'name', 'category')

class CommentAdmin(admin.ModelAdmin):
    list_display  = ('id', 'text', 'user', 'article')


class PresentsAdmin(admin.ModelAdmin):
    list_display  = ('id', 'text', 'user', 'article')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Presents, PresentsAdmin)
