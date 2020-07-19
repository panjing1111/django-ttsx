"""ttsx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from goods.views import index, detail, goods
from cart.views import add_cart, show_cart, remove_cart

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', index), # 首页
    url(r'^detail/$', detail), # 商品详情页
    url(r'^cart/add_cart/$', add_cart), # 添加商品到购物车
    url(r'^cart/show_cart/$', show_cart), # 购物车页面
    url(r'^cart/remove_cart/$', remove_cart), # 删除购物车中的商品
    url(r'^goods/$', goods), # 商品分类列表页

]
