# Generated by Django 2.2.5 on 2019-09-28 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestMysql', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useinfo',
            old_name='usergroup',
            new_name='user_group',
        ),
    ]