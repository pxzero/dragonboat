# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import pytz
from django.http import HttpResponse

from boat.common.BoatUserStatus import BoatUserStatus
from boat.common.BoatResponse import BoatResponse

# Create your views here.

import json

from boat.models import Boat, BoatFollower, BoatUserHis


def index(request):
    return HttpResponse("Hello Django World")


def become_caption(request):
    if request.method == "POST":
        try:
            jdata = json.loads(request.body)
            boat = Boat()
            boat.boat_topic = jdata["boat_topic"]
            boat.boat_owner = jdata["boat_owner"]
            boat.boat_owner_nick_name = jdata["boat_owner_nick_name"]
            boat.boat_create_time = datetime.datetime.fromtimestamp(jdata["boat_create_time"],
                                                                    pytz.timezone("Asia/Shanghai"))
            boat.boat_distance = 0
            boat.save()
            return BoatResponse.resp(200, "success")
        except Exception as e:
            print(e)
            return BoatResponse.resp(500, "fail")
    else:
        return BoatResponse.resp(405, "fail")


def search_boat(request):
    if request.method == "POST":
        try:
            jdata = json.loads(request.body)
            boat_id = jdata["boat_id"]
            open_id = jdata["open_id"]
            boat_data = Boat.objects.filter(boat_id=boat_id).get()
            top_data = __get_top_data(boat_data)
            user_data = __get_user_data(open_id)
            follower_data = __get_follower_data(boat_data)
            ret_data = {
                "boat_topic": boat_data.boat_topic,
                "boat_owner_nick_name": boat_data.boat_owner_nick_name,
                "boat_create_time": boat_data.boat_create_time,
                "top_data": top_data,
                "user_data": user_data,
                "follower_data": follower_data
            }
            BoatResponse.resp(200, "", ret_data)
        except Exception as e:
            print(e)
            return BoatResponse.resp(500, "server internal error")
    else:
        return BoatResponse.resp(405, "fail")


def become_follower(request):
    if request.method == "POST":
        try:
            jdata = json.loads(request.body)
            user_boat_id = jdata["user_boat_id"]
            user_role = jdata["user_role"]
            if user_role == BoatUserStatus.FRESHER:
                pass
            elif user_role == BoatUserStatus.FOLLOWER:
                boat_id = jdata["boat_id"]
                if boat_id == user_boat_id:
                    return BoatResponse(200, "")
                else:
                    user_id = jdata["open_id"]
                    fdata = BoatFollower.objects.filter(user_id=user_id).get()
                    __save_follower_history(fdata)
                    BoatFollower.objects.filter(user_id=user_id).delete()
            elif user_role == BoatUserStatus.CAPTION:
                boat_id = jdata["boat_id"]
                if boat_id == user_boat_id:
                    return BoatResponse(200, "")
                else:
                    cdata = Boat.objects.filter(boat_id=user_boat_id).get()
                    __save_caption_history(cdata)
                    Boat.objects.filter(boat_id=user_boat_id).delete()
                    BoatFollower.objects.filter(boat_id=user_boat_id).update(boat_id=boat_id)
            else:
                return BoatResponse(400, "user role error!")
            __save_follower(jdata)
            return BoatResponse.resp(200, "")
        except Exception as e:
            print(e)
    else:
        return BoatResponse.resp(405, "fail")


def __save_follower(jdata):
    boat_follower = BoatFollower()
    boat_follower.boat_id = jdata["boat_id"]
    boat_follower.user_id = jdata["open_id"]
    boat_follower.follower_time = datetime.datetime.fromtimestamp(jdata["follower_time"],
                                                                  pytz.timezone("Asia/Shanghai"))
    # get nickname from client or weichat
    boat_follower.nickname = jdata["nickname"]
    boat_follower.save()


def __save_follower_history(fdata):
    his = BoatUserHis()
    if isinstance(fdata, Boat):
        his.boat_id = fdata.boat_id
        his.openid = fdata.user_id
        his.ac_time = datetime.datetime.fromtimestamp(datetime.now,pytz.timezone("Asia/Shanghai"))
        his.ac_ctx = fdata.str()
        his.save()


def __save_caption_history(cdata):
    his = BoatUserHis()
    if isinstance(cdata,Boat):
        his.boat_id = cdata.boat_id
        his.openid = cdata.open_id
        his.ac_time = datetime.datetime.fromtimestamp(datetime.now,pytz.timezone("Asia/Shanghai"))
        his.ac_ctx = cdata.str()
        his.save()


def __get_top_data(boat_data):
    # get from memcache
    return {}


def __get_user_data(open_id):
    resp = {}
    boat = Boat.objects.filter(boat_owner=open_id).first()
    boat_follower = BoatFollower.objects.filter(user_id=open_id).first()
    if boat:
        resp["user_boat_id"] = boat.boat_id
        resp["user_role"] = BoatUserStatus.CAPTION
    else:
        resp["user_boat_id"] = ""
        if boat_follower:
            resp["user_role"] = BoatUserStatus.FOLLOWER
        else:
            resp["user_role"] = BoatUserStatus.FRESHER
    return resp


def __get_follower_data(boat_data):
    resp = {}
    boat_followers = BoatFollower.objects.filter(user_id=boat_data.user_id).all()
    resp["size"] = len(boat_followers)
    data = []
    for boat_follower in boat_followers:
        data += {
            "user_id":boat_follower.user_id,
            "nick_name":boat_follower.nick_name
        }
    resp["data"] = data
    return resp
