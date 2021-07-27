from django.http import Http404
from rest_framework import status, generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Category, Comment
from .serializers import *


class TestView(APIView):

    def post(self, request, format=None):
        number1 = request.data.get("test1")
        number2 = request.data.get("test2")
        print(number1)
        print(number2)
        rez = int(number1) + int(number2)

        return Response(rez, status=status.HTTP_201_CREATED)


class CalculeteView(APIView):

    def post(self, request, format=None):
        number1 = request.data.get("number1")
        number2 = request.data.get("number2")
        deistviy = request.data.get("dev")
        if deistviy == "+":
            rez = int(number1) + int(number2)
        elif deistviy == "-":
            rez = int(number1) - int(number2)
        else:
            rez = "Error"
        return Response(rez, status=status.HTTP_201_CREATED)


class CreatArticleView(APIView):

    def post(self, request, format=None):
        name = request.data.get("name")
        text = request.data.get("text")
        print(name)
        print(text)
        new_article = Article(name = name, text = text)
        new_article.save()
        rez = " "


        return Response(rez, status=status.HTTP_201_CREATED)


class CreateCategory(APIView):

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ListCategory(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()



class ItemArticleViews(APIView):

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ItemArticleSerializer(snippet)
        return Response(serializer.data)

class ListArticle(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.all()


class GetListCommentToArticle(generics.ListAPIView):
    serializer_class = CommentSerializer


    def get_queryset(self):
        pk = self.kwargs['pk']
        return Comment.objects.filter(article_id=pk)

class CreateComment(APIView):

    def post(self, request, format=None):
        serializer = CreateCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id = request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListPresent(generics.ListAPIView):
    serializer_class = PresentsSerializer

    def get_queryset(self):
        return Presents.objects.all()

class GetListPresentsToArticle(generics.ListAPIView):
    serializer_class = PresentsSerializer


    def get_queryset(self):
        pk = self.kwargs['pk']
        return Presents.objects.filter(article_id=pk)


class CreatePresents(APIView):

    def post(self, request, format=None):
        serializer = CreatePresentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id = request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUsernameView(APIView):

    def post(self, request, format=None):
        print("Hello") # тест функции
        print(request.user)
        print(request.user.id)
        user = str(request.user)
        return Response(user, status=status.HTTP_201_CREATED)

class GetCommentToUser(generics.ListAPIView):
    serializer_class = CommentSerializer


    def get_queryset(self):
        pk = self.request.user.id
        return Comment.objects.filter(user_id=pk)