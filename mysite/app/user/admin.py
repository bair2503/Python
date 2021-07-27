from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'iphone', 'mail', 'skype', 'age', 'address')






admin.site.register(Profile, ProfileAdmin)
