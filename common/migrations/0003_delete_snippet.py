# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-20 03:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_snippet'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]