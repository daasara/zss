# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashback', '0006_auto_20170331_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sendsms',
            old_name='user_id',
            new_name='seller_id',
        ),
        migrations.AddField(
            model_name='sendsms',
            name='customer_id',
            field=models.IntegerField(null=True, verbose_name='会员id'),
        ),
    ]
