# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-01-16 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_productcomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomments',
            name='rating',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]),
        ),
    ]
