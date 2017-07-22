# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Boat(models.Model):
    boat_id = models.AutoField(primary_key=True, auto_created=True)
    boat_topic = models.CharField(max_length=255)
    boat_owner = models.CharField(max_length=255)
    boat_create_time = models.DateTimeField()
    boat_destory_time = models.DateTimeField(auto_now=False, null=True)
    boat_distance = models.BigIntegerField()


class BoatFollower(models.Model):
    boat_id = models.ForeignKey(Boat)
    user_id = models.CharField(max_length=255, primary_key=True, db_index=True)
    follower_time = models.DateTimeField(auto_now=True)
    nick_name = models.TextField(max_length=1024)


class BoatUserHis(models.Model):
    his_id = models.AutoField(primary_key=True, auto_created=True)
    boat_id = models.ForeignKey(Boat)
    open_id = models.ForeignKey(BoatFollower)
    ac_time = models.DateTimeField(auto_now=True)
