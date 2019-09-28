from django.shortcuts import render

USER_DICT = {
    '1': {'name': 'root1', 'email': 'root1@xxx.com'},
    '2': {'name': 'root2', 'email': 'root2@xxx.com'},
    '3': {'name': 'root3', 'email': 'root3@xxx.com'},
    '4': {'name': 'root4', 'email': 'root4@xxx.com'},
}


def index(request):
    print(request.path_info)
    return render(request, 'index.html', {'user_dict': USER_DICT})


def detail(request, **kwargs):
    print(request.path_info)
    nid = kwargs.get('nid')
    detail_info = USER_DICT[nid]
    return render(request, "detail.html", {"detail_info": detail_info})
