from django.shortcuts import render, redirect


def login(request):
    if request.method == 'GET':
        return render(request, 'login-1.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'root' and pwd == "123":
            # 生成随机字符串
            # 写到用户浏览器Cookie
            # 保存到Session中
            # 　在随机字符串对应的字典中设置相关内容．．．
            request.session['username'] = user
            request.session['if_login'] = True  # 可不加 直接判断username也可以
            if request.POST.get('session') == '1':  # 单独设置超时时间，当前session生效，不影响全局
                request.session.set_expiry(10)  # 10秒
            return redirect('/index-3/')
        else:
            return redirect('/login-1/')


def index(request):
    # 获取当前用户的随机字符串
    # 根据随机字符串获取对应信息
    if request.session.get('if_login'):
        return render(request, 'index-3.html')
    else:
        return redirect('/login-1/')
