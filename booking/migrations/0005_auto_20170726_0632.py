# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_book_class_of_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='kids',
            field=models.CharField(choices=[('age_1', 'Age btwn 3-11 years'), ('age_2', 'Age above 11 years')], default=None, max_length=10, null=True),
        ),
    ]
