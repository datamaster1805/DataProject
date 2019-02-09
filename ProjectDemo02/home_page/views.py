import datetime

from django.shortcuts import render, redirect

# Create your views here.

from django.core.paginator import Paginator
from django.urls import reverse

from home_page.models import Products


# 主页
from user.models import *


def home_page(request):

    return render(request, 'home.html', locals())


# 产品页面
def products(request, page_num=1):
    # 展示所有产品
    products = Products.objects.all()
    paginator = Paginator(products, 10)

    try:
        page = paginator.page(page_num)
    except Exception as e:
        print(e)
        page = paginator.page(1)

    return render(request, 'products.html', locals())


# 产品详情页面
def product_info(request, p_code):
    # 先判断登录状态

    # 根据点击的产品名称，查找products表，展示产品信息
    product = Products.objects.get(p_code=p_code)

    return render(request, 'product_info.html', locals())


# 购买页面
def buy(request, p_code):
    # 判断客户是否登录
    user_id = request.session.get("user_id")
    if user_id:

        user = User.objects.get(id=user_id)
        # 判断客户是否实名认证
        if user.user_kind == 1:
            # 未实名认证，跳转至认证页面
            return render(request, 'check.html')

        # 根据p_code查询商品，并写入user_products表中
        product = Products.objects.get(p_code=p_code)
        product_id = product.id
        user_id = ''

        return render(request, 'buy.html', locals())
    else:
        return render(request, 'login.html')


# 订单页面
def order(request, p_code, user_id, product_id, money):
    # 根据p_code查询商品，并写入user_products表中
    UserProduct.objects.create(
        p_code=p_code,
        start_date=datetime.datetime.now().strftime('%Y-%m-%d'),
        moeny=money,
        product_id=product_id,
        user_id=user_id,

    )
    return redirect(reverse())


# 资讯页面
def information(request):

    return render(request, 'information.html', locals())


# 帮助页面
def us_page(request):

    return render(request, 'about_us.html', locals())






