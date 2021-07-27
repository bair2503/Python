from django.urls import path, include

from .views import NewsView, ListNews

urlpatterns = [
    path('news/', NewsView.as_view()),
    path('list/news/', ListNews.as_view()),

]