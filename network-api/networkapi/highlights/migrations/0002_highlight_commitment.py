# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-06 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('highlights', '0001_squashed_0007_nullify_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='highlight',
            name='commitment',
            field=models.CharField(blank=True, help_text='Amount of time required', max_length=256),
        ),
    ]
