# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 18:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_auto_20170727_0713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='type_of_ticket',
        ),
        migrations.AlterField(
            model_name='book',
            name='kids',
            field=models.CharField(choices=[('age_1', 'Age btwn 3-11 years'), ('age_2', 'Age above 11 years'), ('no_kid', 'No kid')], default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]