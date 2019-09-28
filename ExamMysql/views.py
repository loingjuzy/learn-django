from django.shortcuts import HttpResponse
from ExamMysql import models


def insert(request):
    BUSINESS_LIST = ['运维', '开发', '市场', '测试']
    for item in range(4):
        models.Business.objects.create(caption=BUSINESS_LIST[item], code='SA')
    models.Host.objects.create(hostname='c1.com', ip='192.168.1.101', port='70', business_id='1')
    models.Host.objects.create(hostname='c2.com', ip='192.168.1.102', port='80', business_id='1')
    models.Host.objects.create(hostname='c3.com', ip='192.168.1.103', port='90', business_id='2')
    return HttpResponse('success')