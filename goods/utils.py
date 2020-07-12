from goods.models import GoodsCategory, GoodsInfo

def get_cart_data(request):
    # 3.购物车商品数据 从cookie中获取 {商品id：数量}
    # 读取购物车商品列表
    cart_goods_list = []
    # 商品总数
    cart_goods_count = 0
    for goods_id, goods_num in request.COOKIES.items():
        if goods_id.isdigit():
            goods_num = int(goods_num)
            cart_goods = GoodsInfo.objects.get(id=goods_id)
            cart_goods.goods_num = goods_num
            cart_goods_list.append(cart_goods)
            cart_goods_count += goods_num
    return cart_goods_list, cart_goods_count