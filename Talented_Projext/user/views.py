import hashlib

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from user.models import *



# 用户登录
def loginView(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        loginname = request.POST.get("loginname")
        loginpwd = request.POST.get("loginpwd")
        md5 = hashlib.md5()
        md5.update(loginpwd.encode("utf-8"))
        loginpwd = md5.hexdigest()
        users = UserInformation.objects.filter(username=loginname, password=loginpwd)
        if users:
            user = users.first()
            request.session["user_id"] = user.id  # 登录成功后，设置session属性
            return redirect(reverse("user:mine"))
        else:
            return redirect(reverse("user:login"))


# 用户注册2
def register(request):
    if request.method == "GET":   # 如果是GET请求，则直接进入注册页面
        return render(request,'index.html')
    elif request.method == "POST":

         username = request.POST.get("r_name")
         userpassword = request.POST.get("r_pwd")
         telephone = request.POST.get("r_tele ")
         email = request.POST.get("r_email")
         age = request.POST.get("r_age")
         sex = request.POST.get("r_sex")

         new_user = UserInformation()
         new_user.username = username
         md5 = hashlib.md5()
         md5.update(userpassword.encode("utf-8"))
         new_user.password = md5.hexdigest()
         new_user.telephone = telephone
         new_user.useremail = email
         new_user.usersex = sex
         new_user.userage = age

         new_user.save()
         request.session["user_id"] = new_user.id  # 登录成功后，设置session属性
         return redirect(reverse("user:success")) #*****返回要跳过来那页*******？


#注册成功跳转页面
def success(request):
    return render(request,"success.html")

page_size = 5
# 用户中心
def mineView(request,pagenum=1,pagenum2=1):
    username = request.user.username
    v = request.session.get('name')
    print(v)
    if v:
        u_product  = UserProduct.objects.all()
        page_size = 5
        paginator = Paginator(u_product, page_size)  # 实例化分页器对象，传入数据源和每页显示的条数
        try:
            page = paginator.page(pagenum)
        except:
            page = paginator.page(1)

        return render(request, 'usermine.html', locals())
    else:
        return redirect(reverse("user:login"))


# 退出登录
def logoutView(request):
    request.session.flush()
    return redirect(reverse("#"))
