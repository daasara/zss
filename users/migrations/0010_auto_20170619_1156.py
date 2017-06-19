# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-19 11:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20170619_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jdusername',
            name='jdUsername',
            field=models.CharField(max_length=30, unique=True, verbose_name='京东账号'),
        ),
        migrations.AlterField(
            model_name='pcguid',
            name='PcGuid',
            field=models.IntegerField(max_length=60, null=True, unique=True, verbose_name='pcGuid'),
        ),
        migrations.AlterField(
            model_name='pcguid',
            name='addtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 6, 19, 11, 56, 32, 791358), null=True, verbose_name='登录验证时间'),
        ),
        migrations.AlterField(
            model_name='pcguidlog',
            name='addtime',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 19, 11, 56, 32, 792088), verbose_name='loginTime'),
        ),
        migrations.AlterField(
            model_name='tbusername',
            name='tbUsername',
            field=models.CharField(max_length=30, unique=True, verbose_name='淘宝账号'),
        ),
        migrations.AlterField(
            model_name='visuallog',
            name='addtime',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 19, 11, 56, 32, 792923), verbose_name='loginTime'),
        ),
    ]
