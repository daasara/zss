# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-16 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobiletask',
            name='mobileid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto.mobileid'),
        ),
    ]