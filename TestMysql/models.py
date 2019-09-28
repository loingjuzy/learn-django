from django.db import models


class UseInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

# 数据库默认创建id列 自增 主键
# 用户名列 字符串类型 字符长度