# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 04:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('boat_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('boat_topic', models.CharField(max_length=255)),
                ('boat_owner', models.CharField(max_length=255)),
                ('boat_create_time', models.DateTimeField(auto_now=True)),
                ('boat_destory_time', models.DateTimeField(blank=True)),
                ('boat_distance', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BoatFollower',
            fields=[
                ('user_id', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False)),
                ('follower_time', models.DateTimeField(auto_now=True)),
                ('nick_name', models.CharField(max_length=255)),
                ('boat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boat.Boat')),
            ],
        ),
    ]
