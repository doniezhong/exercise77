# -*- coding: utf-8 -*-
import base64
import json
import os

from django.conf import settings
from django.http import StreamingHttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from account.decorators import login_exempt
from common.mymako import render_mako_context
from blueking.component.shortcuts import get_client_by_request
from home_application.api_manager import JobApiManager, CCApiManager
from home_application.resource import Chart, TopoTreeHandle
from home_application.utils import now_time, now_time_str, time_operation
from utilities.response import *
from conf.default import APP_ID, APP_TOKEN
from utilities.error import try_exception


def api_test(request):
    # celery
    # my_test.apply_async(args=['HEIHA'], eta=time_operation(now_time(), seconds=10))
    cc_api = CCApiManager(request)
    bizs = cc_api.search_business()
    res = cc_api.search_biz_inst_topo({'bk_biz_id': 3})
    params = {
        "condition": [
            {
                "bk_obj_id": "host",
                "fields": [],
                "condition": []
            }, {
                "bk_obj_id": "biz",
                "fields": [],
                "condition": []
            },
            {
                "bk_obj_id": "object",
                "fields": [],
                "condition": [
                    {
                        "field": "bk_inst_id",
                        "operator": "$eq",
                        "value": 162
                    }
                ]
            }
        ]
    }
    host_res = cc_api.search_host(params)
    for host in host_res['info']:
        if host['module']:
            i = 1
    # cc_api = CCApiManager(request)
    # res = cc_api.search_module({
    #     "bk_biz_id": 2,
    #     "fields": [
    #     ],
    #     "condition": {
    #         "bk_module_id": "13"
    #     },
    #     "page": {
    #         "start": 0,
    #         "limit": 10
    #     }})
    return success_result()