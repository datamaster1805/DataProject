from django.db import models

#
class UserInformation(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    telephone = models.IntegerField(blank=True)
    useremail = models.CharField(max_length=50)
    useridcard = models.CharField(max_length=20)
    usersession = models.CharField(max_length=50)
    jurisdiction = models.IntegerField(null=False,choices=((1,"普通会员"),(2,"超级会员"))) # 权限等级一级、二级
    userage = models.IntegerField()
    usersex = models.CharField(max_length=5,choices=((1,'男'),(2,'女')))


#用户银行卡信息
class BankCardInformation(models.Model):
    cardnumber =  models.IntegerField()
    cardtype = models.CharField(max_length=10)
    cardbank = models.CharField(max_length=10)
    user = models.ForeignKey(UserInformation,on_delete=models.CASCADE)  #  与用户建立一对多关系，一个用户，多张银行卡。



class UserProduct(models.Model):
    p_name = models.CharField(max_length=20)
    p_code = models.IntegerField()
    p_type = models.CharField(max_length=10)
    saleprice = models.DateTimeField()
    pcompany = models.CharField(max_length=10)
    sericecharge = models.FloatField()
    exprice = models.DateTimeField()