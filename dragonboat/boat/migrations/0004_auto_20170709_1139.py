# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0003_boatuserhis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='boat_destory_time',
            field=models.DateTimeField(null=True),
        ),
    ]
