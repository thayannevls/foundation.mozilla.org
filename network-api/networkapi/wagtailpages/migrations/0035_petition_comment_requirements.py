# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-20 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0034_auto_20180727_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='petition',
            name='comment_requirements',
            field=models.CharField(choices=[('none', 'No comments'), ('optional', 'Optional comments'), ('required', 'Required comments')], default='none', help_text='What is the comments policy for this petition?', max_length=8),
        ),
    ]
