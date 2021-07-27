from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from app.news.models import CreatNews, News
from app.news.serializers import NewsSerializer


class NewsView(APIView):

    def post(self, request, format=None):


            return Response("hello", status=status.HTTP_201_CREATED)

class CreatNewsView(APIView):

    def post(self, request, format=None):
        name = request.data.get("name")
        text = request.data.get("text")
        print(name)
        print(text)
        new_news = News(name = name, text = text)
        new_news.save()
        rez = " "


        return Response(rez, status=status.HTTP_201_CREATED)

class ListNews(generics.ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.all()
