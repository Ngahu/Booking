# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 08:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20170726_0634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date_leaving',
        ),
        migrations.AddField(
            model_name='book',
            name='date_travelling',
            field=models.DateField(default=datetime.datetime(2017, 7, 26, 8, 27, 36, 498476, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
