# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 15:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='bid',
            new_name='seller_id',
        ),
    ]