from django.http import HttpResponse
from django.shortcuts import render, redirect

from goods.utils import get_cart_data

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

def show_cart(request):
    '''显示购物车'''
    # 购物车中的商品列表、购物车中的商品总数、购物车中的商品总价
    # cart_goods_list中的一个元素是GoodsInfo对象
    cart_goods_list, cart_goods_count, cart_goods_money = get_cart_data(request, True)
    context = {'cart_goods_list':cart_goods_list,
               'cart_goods_count':cart_goods_count,
               'cart_goods_money':cart_goods_money
               }

    return render(request, 'cart.html', context)

def remove_cart(request):
    '''删除购物城中的一个商品'''
    # 获取要删除的商品id
    goods_id = request.GET.get('id', '')
    # 查看cookie中是否有goods_id
    goods_count = request.COOKIES.get(goods_id)
    # 重定向到当前页面
    prev_url = request.META['HTTP_REFERER']
    response = redirect(prev_url)
    if goods_count:
        # 删除cookie中的商品
        response.delete_cookie(goods_id)

    return response
