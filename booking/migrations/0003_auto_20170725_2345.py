# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20170725_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='kids',
            field=models.CharField(choices=[('age_1', 'Age btwn 3-11 years'), ('age_2', 'Age above 11 years')], max_length=10, null=True),
        ),
    ]
