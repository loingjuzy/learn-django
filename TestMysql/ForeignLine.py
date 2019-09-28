from django.shortcuts import HttpResponse
from TestMysql import models


def add(request):
    ug_obj = models.UseGroup.objects.create(caption = "普通用户")
    # 把外键ug_obj当参数传入
    models.UseInfo.objects.create(username='derek',password='12345',user_group=ug_obj)
    return HttpResponse('11')


def select_join(request):
    v2 = models.UseInfo.objects.filter(id=5).values('id','username','password','user_group_id','user_group__caption')
    print(v2)
    return HttpResponse('33')