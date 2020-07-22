from goods.models import GoodsCategory, GoodsInfo


def get_cart_data(request, price=False):
    '''
    购物车商品数据 从cookie中获取 {商品id：数量}
    :param request:
    :param price: 是否计算价格
    :return:
    '''
    # 购物车商品列表
    cart_goods_list = []
    # 商品总数
    cart_goods_count = 0
    # 购物车的总价
    cart_goods_money = 0
    for goods_id, goods_num in request.COOKIES.items():
        if goods_id.isdigit():
            goods_num = int(goods_num)
            cart_goods = GoodsInfo.objects.get(id=goods_id)
            # cookie中当前商品的数量
            cart_goods.goods_num = goods_num
            cart_goods_list.append(cart_goods)
            cart_goods_count += goods_num
            if price:
                # cookie中当前商品的总价 单价*数量
                cart_goods.total_money = goods_num * cart_goods.goods_price
                cart_goods_money += cart_goods.total_money
    return cart_goods_list, cart_goods_count, cart_goods_money
