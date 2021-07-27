from django.db import models
from pytz import unicode

from app.shop.models import ProductShop


class Status(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return unicode("+" + self.name)


class Order(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    iphone = models.CharField(max_length=200)
    address = models.TextField(null= True, blank=True)



    def __str__(self):
        return unicode("+" + self.name)

class ElementOrder(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(ProductShop, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    prace = models.FloatField(default=0)
    count = models.IntegerField(default=0)



    def __str__(self):
        return unicode("+" + self.name)

