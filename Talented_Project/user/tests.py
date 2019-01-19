from django.test import TestCase

# Create your tests here.
def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        name=request.POST.get('user')
        pwd=request.POST.get('pwd')
        # obj=models.Girl.objects.filter(username=name,passwprd=pwd).first()
        obj = models.Boy.objects.filter(username=name, passwprd=pwd).first()
        if obj:
            #1、生成随机字符串（sessionID）
            #2、通过cookie发送给客户端
            #3、服务端保存{zhanggen随机字符串:{'name':'zhanggen'.'email':'zhanggen@le.com'}}
            request.session['name']=obj.username #在Django 中一句话搞定
            request.session['email'] = 'zhanggen@le.com'
            return redirect('/index')
        else:
            return render(request,'login.html',{'msg':"用户名/密码错误"})

def index(request):
    #1、获取客户端的 sessionID
    #2、在服务端查找是否存在 这个sessionID
    #3、在服务端查看对应的key sessionID键的值中是否有name（有值就是登录过了！！）
    v=request.session.get('name')
    print(v)
    if v:
        return render(request,'index.html',{'msg':v})
    else:return redirect('/login/')








