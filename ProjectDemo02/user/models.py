from django.db import models
from home_page.models import Products


# 用户表
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    telephone = models.CharField(max_length=11, null=True)
    user_email = models.CharField(max_length=50, null=True)
    user_idcard = models.CharField(max_length=20, null=True)
    user_session = models.CharField(max_length=50, null=True)
    user_kind = models.CharField(max_length=1, default='1')  # 权限等级一级、二级
    user_age = models.IntegerField(null=True)
    user_sex = models.CharField(max_length=5, null=True)
    user_product = models.ManyToManyField(Products, through='UserProduct')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'


# 用户银行卡信息
class BankCardInformation(models.Model):
    number = models.CharField(max_length=30, null=True)
    bank = models.CharField(max_length=10, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_banks'


# 用户购买记录表
class UserProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    p_code = models.CharField(max_length=15)
    # 购买日期
    start_date = models.DateTimeField(null=True)
    # 到期日期
    end_date = models.DateTimeField(null=True)
    # 购买金额
    moeny = models.CharField(max_length=20)

    class Meta:
        db_table = 'user_products'
