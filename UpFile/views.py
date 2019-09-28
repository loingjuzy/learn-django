from django.shortcuts import render
import os


def UpFile(request):
    """4.上传文件file"""
    if request.method == 'POST':
        obj = request.FILES.get('files')
        if obj:
            print(obj, obj.name)
            if not os.path.exists('upload'):
                os.mkdir('upload')
            file_path = os.path.join('upload', obj.name)
            with open(file_path, 'wb') as fs:
                for item in obj.chunks():
                    fs.write(item)
        return render(request, 'UpFile.html')
    elif request.method == 'GET':
        return render(request, 'UpFile.html')
    else:
        print('other')
