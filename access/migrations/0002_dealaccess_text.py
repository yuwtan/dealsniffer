# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-17 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealaccess',
            name='text',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]