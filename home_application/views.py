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
from home_application.api_manager import JobApiManager
from home_application.resource import Chart
from home_application.utils import now_time, now_time_str
from utilities.response import *
from conf.default import APP_ID, APP_TOKEN
from utilities.error import try_exception


def home(request):
    return render_mako_context(request, '/home_application/home.html')


def demo(request):
    return render_mako_context(request, '/home_application/demo.html')


def curd(request):
    return render_mako_context(request, '/home_application/curd.html')


def form(request):
    return render_mako_context(request, '/home_application/form.html')


def chart(request):
    return render_mako_context(request, '/home_application/chart.html')


def api_test(request):
    now_time()
    raise Exception(now_time_str())
    script_content = '''#!/bin/bash
CPU=$(top -bn1 | grep load | awk '{printf "%.2f%%", $(NF-2)}')
echo -e "CPU=$CPU"'''
    job_api = JobApiManager(request)
    res = job_api.execute_and_get_log(
        bk_biz_id=2,
        script_content=script_content,
        ip_list=[{
            'ip': '10.0.1.10',
            'bk_cloud_id': 0
        }]
    )
    return success_result(res)


def test(request):
    username = request.user.username
    return success_result(username)


@try_exception('查询业务')
def search_business(request):
    client = get_client_by_request(request)
    params = {
        'bk_app_code': APP_ID,
        'bk_app_secret': APP_TOKEN,
    }
    res = client.cc.search_business(params)
    if not res['result']:
        return fail_result(res['message'])
    return success_result(res['data']['info'])


def aget_my_test(request):
    series = [
        {
            'name': '正序',
            'value': 100,
        },
        {
            'name': '倒序',
            'value': 266,
        }
    ]

    test_chart = Chart('pie', series=series, title='test')
    chart_datas = []
    for i in range(5):
        chart_datas.append(test_chart.chart_data)
    return success_result(chart_datas)



