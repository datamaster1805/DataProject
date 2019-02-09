from django import forms


class UserForm(forms.Form):   # 自定义用户信息表单类
    u_idcard = forms.IntegerField(label="身份证号码")
    u_email = forms.CharField(max_length=40, label="请输入您的邮箱")
    u_sex = forms.ChoiceField(label="您的性别", choices=(("1", "男"), ("2", "女")))
    u_age = forms.IntegerField(label="请输入年龄")


bank_name = (

    ("1", "中国银行"),
    ("2", "中国工商银行"),
    ("3", "中国建设银行")
)
card_type = (
    ("1", "信用卡"),
    ("2", "储蓄卡"),
    ("3", "借记卡")
     )


class UserBankCardForm(forms.Form):   # 自定义银行卡信息表单类
    c_number = forms.IntegerField(label="卡号")
    c_bank = forms.ChoiceField(label="银行信息", choices=bank_name)
    #c_type = forms.ChoiceField(label="卡的类型", choices=card_type)
