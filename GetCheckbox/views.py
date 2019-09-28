from django.shortcuts import render


def GetCheckbox(request):
    """3.获取checkbox多个值"""
    if request.method == 'POST':
        favor_list = request.POST.getlist('favor')
        print(favor_list)
        return render(request, 'getcheckbox.html')
    elif request.method == 'GET':
        return render(request, 'getcheckbox.html')
    else:
        print('other')
