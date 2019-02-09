import hashlib
import uuid

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from user.models import *
from user.forms import *


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
            request.session["user_id"] = str(user.id) + str(uuid.uuid4())    # 登录成功后，设置session属性
            session_id = request.session.get("user_id")
            print(session_id)
            user.user_session =session_id
            user.save()
            return redirect(reverse("user:mine", args=(1, 1)))
        else:
            return redirect(reverse("user:login"))


# 用户手机号验证
def check(request):
    if request.method == "GET":  # 如果是GET请求，则直接进入注册页面
            return render(request, 'check.html')
    elif request.method == "POST":
        # 判断电话验证码
        telephone = request.POST.get("phoneNo")
        request.session['user_phone'] = telephone
        t_code = request.POST.get("t_code")
        # new_user = User()
        # new_user.telephone = telephone
        # new_user.save()
        if t_code == "6":
            # return redirect(reverse("user:register", kwargs={'telephone': telephone}))
            return redirect(reverse("user:register"))
        else:
            return render(request, 'check.html')


# 用户注册

# def register(request, telephone):
def register(request):
    if request.method == "GET":   # 如果是GET请求，则直接进入注册页面
        # telephone = telephone
        user_phone = request.session.get('user_phone')
        if not user_phone:
            return render(request, 'check.html')
        else:
            return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get("r_name")
        userpassword = request.POST.get("r_pwd")
        new_user = User()
        new_user.username = username
        md5 = hashlib.md5()
        md5.update(userpassword.encode("utf-8"))
        new_user.password = md5.hexdigest()
        new_user.telephone = request.session.get('user_phone')
        new_user.save()
        request.session['user_phone'] = ''

        request.session["user_id"] = str(new_user.id) + str(uuid.uuid4())
        session_id = request.session.get("user_id")
        print(session_id)
        new_user.user_session = session_id
        new_user.save()
        return redirect(reverse("user:register_form"))   # *****返回要跳过来那页*******？


#  注册成功跳转页面
def success(request):
    return render(request, "success.html")


# 用户中心
def mineView(request, page_one=1, page_tow=1):
    # username = request.
    session_id = request.session.get('user_id')
    print(session_id)
    if session_id:
        page_size = 5
        user = User.objects.get(user_session=session_id)
        print(user.username)
        user_id = user.id

        user_product = UserProduct.objects.filter(user_id=user_id)

        paginator = Paginator(user_product, page_size)  # 实例化分页器对象，传入数据源和每页显示的条数
        try:
            page = paginator.page(page_one)
        except:
            page = paginator.page(1)

        products = Products.objects.all()
        paginator_tow = Paginator(products, page_size)  # 实例化分页器对象，传入数据源和每页显示的条数
        try:
            page1 = paginator_tow.page(page_tow)
        except:
            page1 = paginator_tow.page(1)

        return render(request, 'mine_user.html', locals())
    else:
        return redirect(reverse("user:login"))


# 表单信息
def u_informastion(request):    # form表单
    session_id = request.session.get('user_id')
    print(session_id)
    if session_id:  # name
        if request.method == "GET":  # 如果是GET请求，则直接进入注册页面
            Userform = UserForm()  # 实例化一个空表单对象
            Bankcardform = UserBankCardForm()
            Bankcardform.c_number = 55555
            return render(request, 'register_form.html', locals())

        if request.method == "POST":
            Bankcardform = UserBankCardForm(request.POST)  # 接收POST提交数据，并将数据封装到表单对象中
            Userform =UserForm(request.POST)
            if Userform.is_valid() and Bankcardform.is_valid():
                u_email = Userform.cleaned_data["u_email"]
                u_age = Userform.cleaned_data["u_age"]
                u_idcard = Userform.cleaned_data["u_idcard"]
                u_sex= Userform.cleaned_data["u_sex"]

                new_user = User.objects.get(user_session=session_id)
                new_user.user_email = u_email
                new_user.user_sex = u_sex
                new_user.user_age = u_age
                new_user.user_idcard = u_idcard
                new_user.user_kind = "2"
                new_user.save()

                b_number = Bankcardform.cleaned_data["c_number"]
                #b_type = Bankcardform.cleaned_data["c_type"]
                b_bank = Bankcardform.cleaned_data["c_bank"]


                new_bankcard = BankCardInformation()
                new_bankcard.number = b_number
                #new_bankcard.cardtype = b_type
                new_bankcard.bank = b_bank
                new_bankcard.user = new_user
                new_bankcard.save()

                return redirect(reverse("user:success"))
            else:
                return redirect(reverse("user:register_form"))
    else:
        return redirect(reverse("user:login"))


# 退出登录
def logoutView(request):
    request.session.flush()
    return redirect(reverse("home_page:home"))
