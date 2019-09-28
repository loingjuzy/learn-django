from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    """1.获取表单提交类型做相应处理，用户名密码输正确跳转到页面，输入错误有提示信息"""
    error_msg = ''
    if request.method == 'POST':
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        if user == 'root' and pwd == '123':
            return redirect('/home')
        else:
            error_msg = '账号或者密码错误'
    return render(request, 'login.html', {'error_msg': error_msg})


USER_LIST = [
    {'id': 1, 'username': 'derek', 'email': '111', "gender": '男'},
    {'id': 2, 'username': 'jack', 'email': '222', "gender": '女'},
    {"id": 3, 'username': 'tom', 'email': '333', "gender": '男'},
]


def home(request):
    """2.模拟数据库交互"""
    if request.method == 'POST':
        temp = {
                'username': request.POST.get('username'),
                'email': request.POST.get('email'),
                'gender': request.POST.get('gender')
                }
        USER_LIST.append(temp)
    return render(request, 'home.html', {'user_list': USER_LIST})
