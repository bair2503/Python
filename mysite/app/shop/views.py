import json

import requests
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CategoryShop, ProductShop
from .serializers import CategoryShopSerializer, ProductShopSerializer


class getValut(APIView):

    def get(self, request, format=None):
        response = requests.get("https://www.cbr-xml-daily.ru/latest.js")
        print(response.text)
        response = json.loads(response.text)
        return Response(round(response.get("rates").get("USD"),3) , status=status.HTTP_201_CREATED)

class ListCategoryShop(generics.ListAPIView):
    serializer_class = CategoryShopSerializer

    def get_queryset(self):
        return CategoryShop.objects.all()

class ListProductShop(generics.ListAPIView):
    serializer_class = ProductShopSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return ProductShop.objects.filter(category_id=pk)


