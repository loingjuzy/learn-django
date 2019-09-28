from django.shortcuts import render
from TestMysql import models


def insert_data(request):
    # 插入数据
    for item in range(5):
        models.UseInfo.objects.create(username='derek' + str(item),password='666' + str(item))
    return render(request, 'message.html', {'msg': '插入成功'})


def select_data(request):
    # 查询数据
    result = models.UseInfo.objects.all()
    print(result)   #QuerySetL类型
    for row in result:
        print(row.id, row.username, row.password, row.user_group_id)
    return render(request, 'message.html', {'msg': '查询成功'})


def update_data(request):
    # 更新数据
    models.UseInfo.objects.filter(id=5).update(user_group_id=2)
    return render(request, 'message.html', {'msg': '更新成功'})


def delete_data(request):
    # 删除数据
    models.UseInfo.objects.filter(id=3).delete()
    return render(request, 'message.html', {'msg': '删除成功'})


def delete_group(request):
    # 删除数据
    try:
        models.UseGroup.objects.filter(id=2).delete()
        return render(request, 'message.html', {'msg': '删除成功'})
    except Exception as e:
        print("未知错误", e)