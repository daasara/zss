# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-06 10:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20170706_1042'),
        ('cryapp', '0009_auto_20170705_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryorder',
            name='jdUsername',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jdid', to='users.jdUsername'),
        ),
        migrations.AddField(
            model_name='cryorder',
            name='tbUsername',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tbid', to='users.tbUsername'),
        ),
    ]
