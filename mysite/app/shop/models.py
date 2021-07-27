from django.db import models
from pytz import unicode


class CategoryShop(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return unicode("+" + self.name)

class ProductShop(models.Model):

    category = models.ForeignKey(CategoryShop, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    logo = models.ImageField('logo', null=True, blank=True, upload_to='logo')
    logo_width = models.IntegerField(default=0)
    logo_height = models.IntegerField(default=0)
    prace = models.FloatField(default=0)

    def __str__(self):
        return unicode("+" + self.name)
