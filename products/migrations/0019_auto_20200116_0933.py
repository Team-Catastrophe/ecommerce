# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-01-16 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20200116_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomments',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
