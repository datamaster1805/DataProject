from django.shortcuts import render

# Create your views here.

from django.core.paginator import Paginator

from home_page.models import Products


# 主页
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
def product_info(request, p_name):
    # 先判断登录状态

    # 根据点击的产品名称，查找products表，展示产品信息
    product = Products.objects.get(p_name=p_name)

    return render(request, 'product_info.html', locals())


# 购买页面
def buy(request, p_code):
    # 判断客户是否实名认证

    return render(request, 'buy.html', locals())


# 资讯页面
def information(request):

    return render(request, 'information.html', locals())


# 帮助页面
def us_page(request):

    return render(request, 'about_us.html', locals())






