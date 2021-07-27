from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Category, Article, Comment, Presents


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "viziboll", "name"]
        #fields = '__all__'

class ItemArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        #fields = ["id", "viziboll"]
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=False)
    all_category = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = Article
        #fields = ["id", "viziboll"]
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username"]
        #fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)
    article = ArticleSerializer(read_only=True, many=False)
    class Meta:
        model = Comment
        #fields = ["id", "viziboll"]
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username"]
        #fields = '__all__'


class PresentsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Presents
        #fields = ["id", "viziboll"]
        fields = '__all__'



class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        #fields = ["id", "viziboll"]
        fields = '__all__'



class CreatePresentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presents
        #fields = ["id", "viziboll"]
        fields = '__all__'