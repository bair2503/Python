from rest_framework import serializers

from .models import Order, ElementOrder, Status
from ..shop.serializers import ProductShopSerializer

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        #fields = ["id", "viziboll", "name"]
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True, many=False)
    class Meta:
        model = Order
        #fields = ["id", "viziboll", "name"]
        fields = '__all__'

class ElementOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElementOrder
        #fields = ["id", "viziboll", "name"]
        fields = '__all__'

class ElementSerializer(serializers.ModelSerializer):
    product = ProductShopSerializer(read_only=True, many=False)
    class Meta:
        model = ElementOrder
        #fields = ["id", "viziboll"]
        fields = '__all__'

