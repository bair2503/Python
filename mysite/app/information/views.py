from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from app.article.models import Presents
from app.article.serializers import PresentsSerializer
from app.information.models import Information, ElementInformation
from app.information.serializers import InformationSerializer, ElementInformationSerializer


class InfomatView(APIView):

    def post(self, request, format=None):


            return Response("hello", status=status.HTTP_201_CREATED)

class CreatInfomatView(APIView):

    def post(self, request, format=None):
        name = request.data.get("name")
        text = request.data.get("text")
        print(name)
        print(text)
        new_news = Information(name = name, text = text)
        new_news.save()
        rez = " "


        return Response(rez, status=status.HTTP_201_CREATED)

class ListInfomat(generics.ListAPIView):
    serializer_class = InformationSerializer

    def get_queryset(self):
        return Information.objects.all()



class ListElementInfo(generics.ListAPIView):
    serializer_class = ElementInformationSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return ElementInformation.objects.filter(information_id=pk)

class ListAllPresents(generics.ListAPIView):
    serializer_class = PresentsSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Presents.objects.filter(user_id =pk)