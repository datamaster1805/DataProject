import hashlib

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse



from user.models import User

# 用户登录
def loginView(request):

    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        loginname = request.POST.get("loginname")
        loginpwd = request.POST.get("loginpwd")
        md5 = hashlib.md5()
        md5.update(loginpwd.encode("utf-8"))
        loginpwd = md5.hexdigest()
        users = User.objects.filter(username=loginname, password=loginpwd)
        if users:
            user = users.first()
            request.session["user_id"] = user.id  # 登录成功后，设置session属性

            return redirect(reverse("T-user:base"))
        else:
            return redirect(reverse("T-user:login"))

    request.session.flush()
    return redirect(reverse("T-user:base"))
#用户注册
def register01(request):
    if request.method == "GET":  # 如果是GET请求，则直接进入注册页面
        return render(request, 'register01.html', locals())
    if request.method == "POST":
        return render(request, 'check.html')
def register(request):
    if request.method == "GET":   # 如果是GET请求，则直接进入注册页面
        return render(request, 'check.html')
    if request.method == "POST":
        pass

# 用户中心
def homeView(request):
    return render(request, 'index.html', locals())
# 退出登录
def logoutView(request):
    pass