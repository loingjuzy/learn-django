from django.db import models


class Business(models.Model):
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32)


class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32, db_index=True)
    ip = models.GenericIPAddressField(protocol='both', db_index=True)
    port = models.IntegerField()
    business = models.ForeignKey(to='Business', to_field='id', on_delete=models.CASCADE)


class Computer(models.Model):
    hostname = models.CharField(max_length=32)
    port = models.IntegerField()


class HostAdmin(models.Model):
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    host = models.ManyToManyField('Computer')
