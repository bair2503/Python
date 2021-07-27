from django.contrib import admin

from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display  = ("id", 'name', 'iphone', 'address' )

class ElementOrderAdmin(admin.ModelAdmin):
    list_display  = ("id", 'name', 'prace', 'count')

class StatusAdmin(admin.ModelAdmin):
    list_display  = ('id', 'name')


admin.site.register(Order, OrderAdmin)
admin.site.register(ElementOrder, ElementOrderAdmin)
admin.site.register(Status, StatusAdmin)