from django.db import models

#
class UserInformation(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    telephone = models.IntegerField(max_length=15,blank=True)
    useremail = models.CharField(max_length=50)
    useridcard = models.CharField(max_length=20)
    usersession = models.CharField(max_length=50)
    jurisdiction = models.IntegerField(max_length=5,null=False,choices=(1,2)) # 权限等级一级、二级
    userage = models.IntegerField(max_length=10)
    usersex = models.CharField(max_length=5,choices=((1,'男'),(2,'女')))


#用户银行卡信息
class BankCardInformation(models.Model):
    cardnumber =  models.IntegerField(max_length=15)
    cardtype = models.CharField(max_length=10)
    cardbank = models.CharField(max_length=10)
    user = models.ForeignKey(UserInformation,on_delete=models.CASCADE)  #  与用户建立一对多关系，一个用户，多张银行卡。



class ProductForm(models.Model):
    productname = models.CharField(max_length=20)
    p_code = models.IntegerField(max_length=10)
    p_type = models.CharField(max_length=10)
    saleprice = models.IntegerField(max_length=10)
    pcompany = models.CharField(max_length=10)
    sericecharge = models.FloatField(max_length=10)