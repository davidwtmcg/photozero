# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 15:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0003_auto_20160125_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='content',
            new_name='desription',
        ),
    ]
