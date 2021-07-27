from django.contrib import admin

from .models import Information, ElementInformation


class InformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class ElementInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'logo','text' )


admin.site.register(Information, InformationAdmin)
admin.site.register(ElementInformation, ElementInformationAdmin)