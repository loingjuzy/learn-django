"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from cmdb import views as cm
from GetCheckbox import views as gc
from UpFile import views as uf
from RouterRules import views as rr
from TestMysql import OperateMysql, ForeignLine
from ExamMysql import views as ex
from TempLanguage import views as tl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('cmdb.urls')),  # 5.路由分发
    path('home/', cm.home),
    path('getcheckbox/', gc.GetCheckbox),
    path('UpFile/', uf.UpFile),
    path('index/', rr.index),
    re_path(r'detail-(?P<nid>\d+)-(?P<uid>\d+).html/', rr.detail, name='i3'),
    path('insert/', OperateMysql.insert_data),
    path('select/', OperateMysql.select_data),
    path('update/', OperateMysql.update_data),
    path('delete/', OperateMysql.delete_data),
    path('delete_group/', OperateMysql.delete_group),
    path('foreign/', ForeignLine.add),
    path('select_join/', ForeignLine.select_join),
    path('example/', ex.insert),
    path('business/', ex.business),
    path('host/', ex.host),
    path('add_host/', ex.add_host),
    path('add_hostadmin/', ex.add_hostadmin),
    path('user_info/', ex.user_info),
    path('user_list/', tl.user_list),

]
