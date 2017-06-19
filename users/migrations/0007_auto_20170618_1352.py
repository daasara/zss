# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-18 13:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20170618_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='jdusername',
            name='is_blacklist',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='blacklist'),
        ),
        migrations.AddField(
            model_name='pcguid',
            name='is_blacklist',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='blacklist'),
        ),
        migrations.AddField(
            model_name='tbusername',
            name='is_blacklist',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='blacklist'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='is_blacklist',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='blacklist'),
        ),
        migrations.AlterField(
            model_name='pcguid',
            name='addtime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 6, 18, 13, 52, 50, 600454), null=True, verbose_name='登录验证时间'),
        ),
        migrations.AlterField(
            model_name='pcguidlog',
            name='addtime',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 18, 13, 52, 50, 601081), verbose_name='loginTime'),
        ),
    ]
