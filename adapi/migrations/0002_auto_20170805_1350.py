# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-05 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='thumb',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='advert',
            name='url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='advert',
            name='timeline',
            field=models.IntegerField(null=True),
        ),
    ]
