"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/article/', include('app.article.urls')),
    path('api/v1/auth/', include('djoser.urls')), #????
    path('api/v1/auth-token/', include('djoser.urls.authtoken')),
    path('api/v1/user/', include('app.user.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('api/v1/news/', include('app.news.urls')),
    path('api/v1/information/', include('app.information.urls')),
    path('api/v1/shop/', include('app.shop.urls')),
    path('api/v1/order/', include('app.order.urls')),
]
