from django.urls import path, include

from .views import *

urlpatterns = [
    path('user/item/', ItemUserViews.as_view()),
    path('list/user/', ListUser.as_view()),
    path('user/profile/', CreatProfile.as_view()),
    path('item/profile/', ItemProfile.as_view()),
    path('patch/profile/', PatchProfileViews.as_view()),

]