# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-26 03:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_nullify_homepage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='glyph',
        ),
    ]