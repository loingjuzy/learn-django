# Generated by Django 2.2.5 on 2019-09-28 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32)),
                ('code', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(db_index=True, max_length=32)),
                ('ip', models.GenericIPAddressField(db_index=True)),
                ('port', models.IntegerField()),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExamMysql.Business')),
            ],
        ),
    ]
