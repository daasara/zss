# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-18 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0004_auto_20170717_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobileid',
            name='webserverurl',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
