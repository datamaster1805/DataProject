from django.urls import path

from user import views
app_name = 'T-user'
urlpatterns = [
    # 用户中心
    path('home/', views.homeView, name='home'),
    # 用户的注册和登录
    path('login/', views.loginView, name='login'),
    path('register/', views.register, name='register'),
    path('register01/', views.register01, name='register01'),
    # 退出用户登录
    path('logout/', views.logoutView, name='logout'),
]
