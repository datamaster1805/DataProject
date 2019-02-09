from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    # 用户中心
    path('mine/<int:page_one>/<int:page_tow>/', views.mineView, name='mine'),
    # 用户的注册和登录
    path('login/', views.loginView, name='login'),
    # path('register/<str:telephone>/', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('check/', views.check, name='check'),
    path('register_form/', views.u_informastion, name='register_form'),
    path('register_success/', views.success, name='success'),
    # 退出用户登录
    path('logout/', views.logoutView, name='logout'),
]
