# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 15:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='customer_id',
            field=models.IntegerField(null=True, verbose_name='会员'),
        ),
        migrations.AddField(
            model_name='order',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='商家'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(null=True, verbose_name='订单状态'),
        ),
    ]