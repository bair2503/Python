from django.urls import path, include

from .views import *


urlpatterns = [
    path('information/', InfomatView.as_view()),
    path('list/information/', ListInfomat.as_view()),
    path('item/information/<int:pk>/', ListElementInfo.as_view()),
    path('list/present/<int:pk>/', ListAllPresents.as_view()),
]