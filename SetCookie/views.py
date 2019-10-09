from django.core.paginator import Page
from django.shortcuts import render, redirect

from TempLanguage.views import LIST

user_info = {
    'derek': {'pwd': '123123'},
    'jack': {'pwd': '456456'}
}


def login(request):
    if request.method == 'GET':
        return render(request, 'login-0.html')

    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        dic = user_info.get(u)  # 获取key的value
        if not dic:
            return render(request, 'login-0.html')
        if dic['pwd'] == p:
            result = redirect('/index-2/')
            result.set_cookie('username', u)  # 设置cookie值
            # result.set_cookie('username', u, max_age=10)  # 设置cookie失效时间10s
            # 第二种方法 设置失效时间
            import datetime
            current_date = datetime.datetime.utcnow()  # 获取当前时间
            current_date = current_date + datetime.timedelta(seconds=5)
            result.set_cookie('username', u, expires=current_date)

            return result
        else:
            return render(request, 'login-0.html')


def index(request):
    v = request.COOKIES.get('username')
    if not v:
        return redirect('/login-0/')
    return render(request, 'index-2.html', {'current_user': v})


def user_list(request):
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)

    per_page_count = request.COOKIES.get('per_page_count', 10)  # 获取cookie值
    per_page_count = int(per_page_count)

    page_obj = Page(current_page, len(LIST), per_page_count)

    data = LIST[page_obj.start:page_obj.end]

    page_str = page_obj.page_str("/user_list/")

    return render(request, 'user_list.html', {'li': data, 'page_str': page_str})
