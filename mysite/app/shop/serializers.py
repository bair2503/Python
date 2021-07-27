from rest_framework import serializers

from .models import CategoryShop, ProductShop


class CategoryShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryShop
        #fields = ["id", "viziboll", "name"]
        fields = '__all__'

class ProductShopSerializer(serializers.ModelSerializer):
    category = CategoryShopSerializer(read_only=True, many=False)
    class Meta:
        model = ProductShop
        #fields = ["id", "viziboll"]
        fields = '__all__'

