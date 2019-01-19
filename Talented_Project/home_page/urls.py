from django.contrib import admin
from django.urls import path
from home_page.views import *

app_name = 'home_page'

urlpatterns = [
    path('index/', home_apge),
]
