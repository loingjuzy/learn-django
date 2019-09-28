from django.db import models


class UseInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    user_group = models.ForeignKey('UseGroup', on_delete=models.CASCADE, to_field='uid', default=1)


class UseGroup(models.Model):
    uid = models.AutoField(primary_key=True)  # 主键
    caption = models.CharField(max_length=32, null=True)  # 唯一索引
    ctime = models.DateField(auto_now_add=True, null=True)  # 创建时生成时间
    uptime = models.DateField(auto_now=True, null=True)  # 更新时自动更新时间
