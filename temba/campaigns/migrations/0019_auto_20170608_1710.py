# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-08 17:10
from __future__ import absolute_import, division, print_function, unicode_literals

from django.db import migrations
import temba.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0018_auto_20170606_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignevent',
            name='message',
            field=temba.utils.models.TranslatableField(max_length=640, null=True),
        ),
    ]
