from django.contrib import admin
from django.urls import path
from home_page.views import *

app_name = 'home_page'

urlpatterns = [
    path('index/', home_page, name='home'),
    path('products/<int:page_num>/', products, name='products'),
    path('products/info/<str:p_name>/', product_info, name='product_info'),
    path('buy/<p_code>/', buy, name='buy'),
    path('info/', information, name='info'),
    path('help/', us_page, name='us'),
]
