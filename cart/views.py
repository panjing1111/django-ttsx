from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def add_cart(request):
    '''添加商品到购物车,业务逻辑为：在点击添加购物车后，右上角购物车中的数字+1，同时刷新页面
     购物车的保存内容为：{商品id：数量}
     '''
    goods_id = request.GET.get('id')
    # 查看cookie中是否有goods_id
    goods_count = request.COOKIES.get(goods_id)
    if goods_count:
        goods_count = int(goods_count) + 1
    else:
        goods_count = 1

    # 重定向到商品详情页，返回的是HttpResponse对象,在HttpResponse对象中设置购物车cookie
    # 从request中获取访问当前视图函数的url，即商品详情页
    prev_url = request.META['HTTP_REFERER']
    response = redirect(prev_url)
    response.set_cookie(goods_id, goods_count)
    return response



