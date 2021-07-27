from django.urls import path, include

from .views import *

urlpatterns = [
    path('valute/', getValut.as_view()),
    path('list/category/', ListCategoryShop.as_view()),
    path('list/product/<int:pk>/', ListProductShop.as_view()),


]