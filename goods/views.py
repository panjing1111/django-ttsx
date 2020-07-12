from django.shortcuts import render

from goods.models import GoodsCategory, GoodsInfo

from goods.utils import get_cart_data
# Create your views here.


def index(request):
    '''
    首页页面主要展示的数据包括:
        产品的分类数据
        每个分类的产品数据
        购物车商品数据
    '''
    # 1.产品的分类数据
    categories = GoodsCategory.objects.all()
    # 2.每个分类的产品数据 每个分类的最后四个产品数据
    for cag in categories:
        # GoodsInfo.objects.filter(goods_cag=cag)[-4:]
        # 通过一查询多， 一调用
        # cag.goods_list是新创建的变量 用来保存类别对应的4个最近的商品
        cag.goods_list = cag.goodsinfo_set.order_by('-id')[:4]
    # 3.购物车商品数据 从cookie中获取 {商品id：数量}
    cart_goods_list, cart_goods_count = get_cart_data(request)
    context = {'categories':categories,
               "cart_goods_list":cart_goods_list,
               "cart_goods_count":cart_goods_count}
    return render(request, 'index.html',context)

def detail(request):
    '''商品详情页'''
    # 当前商品的数据
    goods_data = GoodsInfo.objects.get(id=request.GET.get('id'))
    # 商品分类
    categories = GoodsCategory.objects.all()
    # 购物车数据
    cart_goods_list, cart_goods_count = get_cart_data(request)

    context = {'categories':categories,
               "cart_goods_list":cart_goods_list,
               "cart_goods_count":cart_goods_count,
               "goods_data":goods_data}
    return render(request, 'detail.html',context)
