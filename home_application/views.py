# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from account.decorators import login_exempt
from common.mymako import render_mako_context
from blueking.component.shortcuts import ComponentClient
from utilities.response import *
from conf.default import APP_ID, APP_TOKEN
from utilities.error import try_exception
from utilities.jobman import JobMan
import json

def home(request):
    return render_mako_context(request, '/home_application/home.html')


def demo(request):
    return render_mako_context(request, '/home_application/demo.html')


def test(request):
    username = request.user.username
    return success_result(username)


@try_exception('查询业务')
def search_business(request):
    client = ComponentClient()
    params = {
        'bk_app_code': APP_ID,
        'bk_app_secret': APP_TOKEN,
        'bk_username': 'admin',
    }
    res = client.cc.search_business(params)
    if not res['result']:
        return fail_result(res['message'])
    return success_result(res['data']['info'])


@try_exception('查询主机')
def search_host(request):
    biz_id = request.GET.get('biz_id')
    # rq_data = json.loads(request.body)
    # ip = rq_data['bk_host_innerip']
    params = {
        'bk_app_code': APP_ID,
        'bk_app_secret': APP_TOKEN,
        'bk_username': 'admin',
        "condition": [
            {
                "bk_obj_id": "host",
                "fields": [],
                "condition": [
                    # {
                    #     "field": "bk_host_innerip",
                    #     "operator": "$regex",
                    #     "value": ip
                    # }
                ]
            },
            {
                "bk_obj_id": "biz",
                "fields": [],
                "condition": [
                    {
                        "field": "bk_biz_id",
                        "operator": "$eq",
                        "value": int(biz_id)
                    }
                ]
            }
        ]
    }
    client = ComponentClient()
    res = client.cc.search_host(params)
    if not res['result']:
        return fail_result(res['message'])
    return success_result(res['data']['info'])

