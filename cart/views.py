import time

from django.http import HttpResponse
from django.shortcuts import render, redirect

from cart.models import OrderInfo, OrderGoods
from goods.models import GoodsInfo
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

def place_order(request):
    '''提交订单页面'''
    cart_goods_list, cart_goods_count, cart_goods_money = get_cart_data(request, True)
    context = {'cart_goods_list': cart_goods_list,
               'cart_goods_count': cart_goods_count,
               'cart_goods_money': cart_goods_money,
               }

    return render(request, 'place_order.html', context)

def submit_order(request):
    '''提交订单的时候将订单保存到数据库'''

    # 获取表单中的信息
    addr = request.POST.get('addr')
    recv = request.POST.get('recv')
    tele = request.POST.get('tele')
    if not tele:
        prev_url = request.META['HTTP_REFERER']
        return redirect(prev_url)
    extra = request.POST.get('extra', )
    # 保存表单提交的信息到数据库
    order_info = OrderInfo()
    order_info.order_addr = addr
    order_info.order_tele = tele
    order_info.order_recv = recv
    order_info.order_extra = extra
    order_info.order_id = str(int(time.time() * 1000)) + str(int(time.clock() * 1000000))
    order_info.save()
    # 保存后需要跳转到订单提交成功页面
    response = redirect('/cart/submit_success/?id=%s' % order_info.order_id)
    # 保存订单商品信息
    for goods_id, goods_num in request.COOKIES.items():
        if goods_id == 'csrftoken':
            continue
        # 查询商品信息
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 创建订单商品信息
        order_goods = OrderGoods()
        order_goods.goods_info = cart_goods
        order_goods.goods_order = order_info
        order_goods.goods_num = goods_num
        order_goods.save()
        # 删除购物车信息
        response.delete_cookie(goods_id)

    return response

def submit_success(request):
    order_id = request.GET.get('id')
    order_info = OrderInfo.objects.get(order_id=order_id)
    # 通过订单查询商品
    order_goods_list = OrderGoods.objects.filter(goods_order=order_info)

    # 商品总价
    totla_money = 0
    # 商品总数量
    total_num = 0
    for goods in order_goods_list:
        goods.total_money = goods.goods_num * goods.goods_info.goods_price
        totla_money += goods.total_money
        total_num += goods.goods_num

    context = {
        'order_goods_list': order_goods_list,
        'totla_money': totla_money,
        'total_num': total_num,
        'order_info':order_info,
    }

    return render(request, 'success.html', context)