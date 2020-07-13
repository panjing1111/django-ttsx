from django.core.paginator import Paginator
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

def goods(request):
    '''商品分类页面'''
    # 当前分类id
    cag_id = request.GET.get('cag')
    page = request.GET.get('page','1')
    # 当前分类下的所有商品 通过一查找多
    current_cag = GoodsCategory.objects.get(id=cag_id)
    goods_data = current_cag.goodsinfo_set.all()
    # 分页器
    paginator = Paginator(goods_data, 12) # 每页12个数据
    page_data = paginator.page(page) # 默认返回第一页的数据
    # 所有分类
    categories = GoodsCategory.objects.all()
    # 购物车
    cart_goods_list, cart_goods_count = get_cart_data(request)
    context = {
        "current_cag":current_cag,
        "categories":categories,
        "page_data":page_data,
        "paginator":paginator,
        "cart_goods_list": cart_goods_list,
        "cart_goods_count": cart_goods_count,

    }
    return render(request,'goods.html',context)