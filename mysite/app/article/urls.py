from django.urls import path, include

from .views import *

urlpatterns = [
    path('test/', TestView.as_view()),
    path('calculete/', CalculeteView.as_view()),
    path('creat/article/', CreatArticleView.as_view()),
    path('creat/category/', CreateCategory.as_view()),
    path('list/category/', ListCategory.as_view()),
    path('item/article/<int:pk>/', ItemArticleViews.as_view()),
    path('list/article/', ListArticle.as_view()),
    path('list/comment/<int:pk>/', GetListCommentToArticle.as_view()),
    path('list/present/<int:pk>/', GetListPresentsToArticle.as_view()),
    path('list/username/', GetUsernameView.as_view()),
    path('create/comment/', CreateComment.as_view()),
    path('create/present/', CreatePresents.as_view()),
    path('user/comment/', GetCommentToUser.as_view()),

]