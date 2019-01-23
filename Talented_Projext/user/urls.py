from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    # 用户中心
    path('mine/', views.mineView, name='mine'),
    path('mine/<pagenum>/', views.mineView, name='mine_num1'),
    path('mine/<pagenum>/<pugenum2>/', views.mineView, name='mine_num2'),
    # 用户的注册和登录
    path('login/', views.loginView, name='login'),
    path('register/', views.register, name='register'),

    path('register_success/', views.success, name='success'),
    # 退出用户登录
    path('logout/', views.logoutView, name='logout'),
]
