from django.http import HttpResponse
import json


class BoatResponse:
    @staticmethod
    def resp(status, msg, data={}):
        response = HttpResponse()
        jdata = {
            "status": status,
            "msg": msg,
            "data": data
        }
        response.content = json.dumps(jdata)
        return response
