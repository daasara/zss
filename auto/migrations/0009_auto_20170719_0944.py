# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-19 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0008_auto_20170718_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobileid',
            name='udid',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='mobiletask',
            name='taskSort',
            field=models.IntegerField(choices=[(1, 'add_User'), (2, 'ADD_GROUP'), (3, 'send_message_to_friend_list'), (4, 'send_message_to_GROUP_list'), (5, 'send_message_to_user_Accoutid'), (6, 'send_message_to_GROUP_Accoutid'), (7, 'Get_Pople_list'), (8, 'Get_Group_list'), (9, 'Get_Group_People_list')], null=True),
        ),
    ]
