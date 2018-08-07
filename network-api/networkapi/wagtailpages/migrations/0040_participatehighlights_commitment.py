# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-06 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0039_participatehighlights'),
    ]

    operations = [
        migrations.AddField(
            model_name='participatehighlights',
            name='commitment',
            field=models.CharField(blank=True, help_text='Amount of time required (eg: "30 min commitment")', max_length=256),
        ),
    ]