from django.shortcuts import render,redirect
from django.http import HttpResponse
#create your views here
from django.urls import reverse

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        #生成响应对象
        res = HttpResponse("生成cookie")
        #max_age 以秒为单位的过期时间
        res.set_cookie('username',username,max_age=3*60*60)
        print(res)
        return res
    return render(request,'app01/login.html')

def reply(request): #获取cookie中的username键对值
    username = request.COOKIES.get('username')
    #username不为空就是登陆过，否则未登录
    if username:
        return HttpResponse("发表评论")
    else:#跳转登陆界面
        # return redirect("/app01/login/")
        return redirect(reverse("App01:login"))

def index(request):#获取cookie
    username = request.COOKIES.get('username')
    print(username)
    return render(request,'app01/index.html',context={'username':username})

def logout(request):#生成响应对象HttpResponseRedirect
    res = redirect(reverse("App01:home"))
    print(res)
    res.delete_cookie('username')
    return res


# Create your views here.
