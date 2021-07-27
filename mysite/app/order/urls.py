from django.urls import path, include

from .veiws import *


urlpatterns = [
    path('list/order/', ListOrder.as_view()),
    path('creat/order/', CreatOrder.as_view()),
    path('creat/element/order/', CreateElementOrder.as_view()),
    path('list/element/order/<int:pk>/', ListElementOrder.as_view()),
    path('patch/order/<int:pk>/', PatchOrderViews.as_view()),
    path('delete/order/<int:pk>/', DeleteOrder.as_view()),

]