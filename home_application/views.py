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
from home_application.celery_tasks import my_test
from home_application.resource import Chart
from home_application.utils import now_time, now_time_str, time_operation
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
    # celery
    my_test.apply_async(args=['HEIHA'], eta=time_operation(now_time(), seconds=10))
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
