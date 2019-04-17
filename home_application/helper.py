# -*- coding: utf-8 -*-
from conf.default import APP_TOKEN, APP_ID
from blueking.component.shortcuts import ComponentClient
from utilities.jobman import JobMan
from utilities.utils import *


def search_cc_host():
    params = {
        'bk_app_code': APP_ID,
        'bk_app_secret': APP_TOKEN,
        'bk_username': 'admin',
        "condition": [
            {
                "bk_obj_id": "host",
                "fields": [],
                "condition": []
            },
            {
                "bk_obj_id": "biz",
                "fields": [],
                "condition": []
            }
        ]
    }
    client = ComponentClient()
    res = client.cc.search_host(params)
    if not res['result']:
        raise Exception('查询失败')
    return res['data']['info']
