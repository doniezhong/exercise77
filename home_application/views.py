# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from account.decorators import login_exempt
from common.mymako import render_mako_context
from blueking.component.shortcuts import ComponentClient
from utilities.response import *
from conf.default import APP_ID, APP_TOKEN


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def demo(request):
    return render_mako_context(request, '/home_application/demo.html')


def search_business(request):
    client = ComponentClient()
    params = {
        'bk_app_code': APP_ID,
        'bk_app_secret': APP_TOKEN,
        'bk_username': 'admin'
    }
    res = client.cc.search_business(params)
    if not res['result']:
        return fail_result(res['message'])
    return success_result(res.data)
