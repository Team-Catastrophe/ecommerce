# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-01-18 03:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_productfaq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
