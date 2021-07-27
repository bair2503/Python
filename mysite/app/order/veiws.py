from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.order.models import Order, ElementOrder
from app.order.serializers import OrderSerializer, ElementOrderSerializer, ElementSerializer


class CreatOrder(APIView):

    def post(self, request, format=None):
        name = request.data.get("name")
        iphone = request.data.get("iphone")
        address = request.data.get("address")

        new_order = Order(name = name, iphone = iphone, address = address )
        new_order.save()
        rez = new_order.id


        return Response(rez, status=status.HTTP_201_CREATED)
    # изменить на сериализатор!!!!

class ListOrder(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

class ListElementOrder(generics.ListAPIView):
    serializer_class = ElementSerializer


    def get_queryset(self):
        pk = self.kwargs['pk']
        return ElementOrder.objects.filter(order_id=pk)



class CreateElementOrder(APIView):

    def post(self, request, format=None):
        serializer = ElementOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatchOrderViews(APIView):

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def patch(self, request, pk):
        testmodel_object = self.get_object(pk)
        serializer = OrderSerializer(testmodel_object, data=request.data,
                                         partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class DeleteOrder(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)