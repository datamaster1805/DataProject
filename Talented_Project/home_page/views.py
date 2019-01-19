from django.shortcuts import render

# Create your views here.
from home_page.models import Products
from django.core.paginator import Paginator


def home_apge(request, page_num=1):
    # 展示所有产品
    products = Products.objects.all()
    paginator = Paginator(products, 5)
    try:
        page = paginator.page(page_num)
    except Exception as e:
        print(e)
        page = paginator.page(1)

    return render(request, 'home.html', locals())
