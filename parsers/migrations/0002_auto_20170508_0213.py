# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parser',
            old_name='filepath',
            new_name='name',
        ),
        migrations.AddField(
            model_name='parser',
            name='parserbody',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
