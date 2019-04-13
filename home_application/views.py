# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from account.decorators import login_exempt
from common.mymako import render_mako_context
from blueking.component.shortcuts import ComponentClient
from utilities.response import *
from conf.default import APP_ID, APP_TOKEN
from utilities.error import try_exception
import json
import sys
from utilities.jobman import JobMan
from home_application.models import IPConfig, HostPerformance


def home(request):
    """
    首页
    """
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
    return success_result(res['data'])


@try_exception('查询主机')
def search_cc_host(request):
    biz_id = request.GET.get('biz_id')
    rq_data = json.loads(request.body)
    ip = rq_data['bk_host_innerip']
    params = {
        'bk_app_code': APP_ID,
        'bk_app_secret': APP_TOKEN,
        'bk_username': 'admin',
        "condition": [
            {
                "bk_obj_id": "host",
                "fields": [],
                "condition": [
                    {
                        "field": "bk_host_innerip",
                        "operator": "$regex",
                        "value": ip
                    }
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
    return_data = []
    for x in res['data']['info']:
        ip = x['host']['bk_host_innerip']
        conf = IPConfig.objects.filter(ip=ip)
        if not len(conf):
            x['is_period'] = False
        else:
            x['is_preiod'] = conf[0].is_period
            x['cpu'] = conf[0].cpu
            x['mem'] = conf[0].mem
            x['disk'] = conf[0].disk
        return_data.append(x)
    return success_result(return_data)


@try_exception('改变主机获取性能状态')
def update_ip_config(request):
    rq_data = json.loads(request.body)
    status = rq_data['status']
    ip = rq_data['ip']
    status = True if status == '1' else False
    conf, is_create = IPConfig.objects.get_or_create(ip=ip)
    conf.is_period = status
    conf.save()
    return success_result(conf.is_period)


@try_exception('查看性能')
def get_ph_by_ip(request):
    rq_data = json.loads(request.body)
    ip = rq_data['ip']
    app_id = rq_data['biz_id']
    job = JobMan()
    host_list = [
        {
            'ip': ip,
            'bk_cloud_id': '0'
        }
    ]
    job_obj = {
        app_id: [
            {
                "host": host_list,
                "script_content": """#!/bin/bash
MEMORY=$(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2 }')
DISK=$(df -h | awk '$NF=="/"{printf "%s", $5}')
CPU=$(top -bn1 | grep load | awk '{printf "%.2f%%", $(NF-2)}')
DATE=$(date "+%Y-%m-%d %H:%M:%S")
echo -e "$DATE|$MEMORY|$DISK|$CPU"
""",
                "script_type": "1",
                "account": "root"
            }
        ]
    }
    job.execute(job_obj)
    _, content = job.get_log(ip)
    s_list = content.split('|')
    s_list = [x for x in s_list if x]
    conf, is_create = IPConfig.objects.get_or_create(ip=ip)
    conf.cpu = float(s_list[3].strip('\n').strip('%'))
    conf.mem = float(s_list[1].strip('\n').strip('%'))
    conf.disk = float(s_list[2].strip('\n').strip('%'))
    conf.save()
    return success_result(
        {
            'cpu': s_list[3],
            'mem': s_list[1],
            'disk': s_list[2],
            'ip': ip,
            'biz_id': app_id
        }
    )


@try_exception('search_ph_host')
def search_ph_host(request):
    ip = IPConfig.objects.all().values()
    return success_result(list(ip))


@try_exception('search_ph_list_by_ip')
def search_ph_list_by_ip(request):
    ip = request.GET.get('ip')
    host = HostPerformance.objects.filter(ip=ip)
    if(len(host) > 30):
        data = list(host.values()[0:30])
    else:
        data = list(host.values())
    return success_result(data)
