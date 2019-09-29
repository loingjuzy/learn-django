from django.shortcuts import HttpResponse, render

from ExamMysql import models


def insert(request):
    BUSINESS_LIST = ['运维', '开发', '市场', '测试']
    for item in range(4):
        models.Business.objects.create(caption=BUSINESS_LIST[item], code='SA')
    models.Host.objects.create(hostname='c1.com', ip='192.168.1.101', port='70', business_id='1')
    models.Host.objects.create(hostname='c2.com', ip='192.168.1.102', port='80', business_id='1')
    models.Host.objects.create(hostname='c3.com', ip='192.168.1.103', port='90', business_id='2')
    return HttpResponse('success')


def business(request):
    # 第一种方式（是个对象）
    v1 = models.Business.objects.all()
    # 第二种方式,只取id和caption（是个字典）
    v2 = models.Business.objects.all().values('id', 'caption')
    return render(request, 'business.html', {'v1': v1, 'v2': v2})


def host(request):
    """总共三种方式，对象，字典，列表"""
    v1 = models.Host.objects.all()
    v2 = models.Host.objects.filter(nid__gt=0).values('nid', 'hostname', 'business__id', 'business__caption')
    v3 = models.Host.objects.filter(nid__gt=0).values_list('nid', 'hostname', 'business__id', 'business__caption')
    return render(request, 'host.html', {'v1': v1, 'v2': v2, 'v3': v3})


# 添加主机信息
def add_host(request):
    models.Computer.objects.create(hostname='host1', port=80)
    models.Computer.objects.create(hostname='host2', port=80)
    models.Computer.objects.create(hostname='host3', port=80)
    models.Computer.objects.create(hostname='host4', port=80)
    return HttpResponse('ok')


# 添加管理用户信息
def add_hostadmin(request):
    models.HostAdmin.objects.create(username='aa', email='11.com')
    models.HostAdmin.objects.create(username='bb', email='22.com')
    models.HostAdmin.objects.create(username='cc', email='33.com')
    models.HostAdmin.objects.create(username='dd', email='44.com')
    return HttpResponse('ok')


# 添加第三张表信息，使管理用户与主机关联
def user_info(request):
    # 第一步找到用户
    admin_obj = models.HostAdmin.objects.get(username='bb')
    # 第二步找到主机
    host_list = models.Computer.objects.filter(id__lt=3)
    # 第三步，通过找到的admin_obj对象.add去添加主机
    admin_obj.host.add(*host_list)

    return HttpResponse('ok')
