# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from account.decorators import login_exempt
from common.mymako import render_mako_context
from blueking.component.shortcuts import ComponentClient
from utilities.response import *
from conf.default import APP_ID, APP_TOKEN
from utilities.error import try_exception
import requests
import json
import sys
from home_application.models import Host
from home_application.models import PH
from utilities.jobman import JobMan

reload(sys)
sys.setdefaultencoding('utf-8')


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def demo(request):
    ip = request.GET.get('ip')
    biz_id = request.GET.get('biz_id')
    return render_mako_context(request, '/home_application/demo.html', {
        'ip': ip,
        'biz_id': biz_id
    })


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


@try_exception('查询业务')
def search_set(request):
    biz_id = request.GET.get('biz_id')
    client = ComponentClient()
    params = {
        'bk_app_code': APP_ID,
        'bk_app_secret': APP_TOKEN,
        'bk_username': 'admin',
        'bk_biz_id': biz_id
    }
    res = client.cc.search_set(params)
    if not res['result']:
        return fail_result(res['message'])
    return success_result(res['data'])


def search_cc_host(request):
    biz_id = request.GET.get('biz_id')
    set_id = request.GET.get('set_id')
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
                "bk_obj_id": "set",
                "fields": [],
                "condition": [
                    {
                        "field": "bk_set_id",
                        "operator": "$eq",
                        "value": int(set_id)
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
    return success_result(res['data'])


@try_exception('查询主机')
def search_host(request):
    ip = request.GET.get('ip')
    host = Host.objects.filter(innerip__icontains=ip).all().values()
    return success_result(list(host))


@try_exception('添加主机')
def add_host(request):
    rq_data = json.loads(request.body)
    host = Host.objects.create(**rq_data)
    return success_result(host.id)


@try_exception('删除主机')
def del_host(request):
    id = request.GET.get('id')
    Host.objects.filter(id=id).delete()
    return success_result()


@try_exception('修改主机')
def update_host(request):
    id = request.GET.get('id')
    rq_data = json.loads(request.body)
    Host.objects.filter(id=id).update(**rq_data)
    return success_result()


@try_exception('查看性能')
def search_ph(request):
    rq_data = json.loads(request.body)
    ph = PH.objects.filter(ip=rq_data['ip']).order_by('-when_created')
    if len(ph) > 12:
        data = list(ph[0: 12].values())
    else:
        data = list(ph.values())
    return success_result(data)


@try_exception('查看内存')
def get_mem(request):
    ip = json.loads(request.body)['ip']
    app_id = json.loads(request.body)['biz_id']
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
                "script_content": "free -m",
                "script_type": "1",
                "account": "root"
            }
        ]
    }
    job.execute(job_obj)
    _, content = job.get_log(ip)
    s_list = content.split('\n')
    mem = s_list[1]
    mem_arr = [x for x in mem.split(' ') if x]
    total = mem_arr[1]
    use = mem_arr[2]
    return success_result(
        [
            {
                'name': '总内存',
                'value': int(total)
            },
            {
                'name': '使用内存',
                'value': int(use)
            }
        ]
    )


@try_exception('查看磁盘')
def get_disk(request):
    ip = json.loads(request.body)['ip']
    app_id = json.loads(request.body)['biz_id']
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
                "script_content": "df -h",
                "script_type": "1",
                "account": "root"
            }
        ]
    }
    job.execute(job_obj)
    _, content = job.get_log(ip)
    s_list = content.split('\n')[1:]
    disk = []
    for s in s_list:
        try:
            s_arr = [x for x in s.split(' ') if x]
            obj = {
                'file': s_arr[0],
                'size': s_arr[1],
                'used': s_arr[2],
                'avail': s_arr[3],
                'use%': s_arr[4],
                'mounted': s_arr[5]
            }
            disk.append(obj)
        except Exception as e:
            print e
    return success_result(
        disk
    )
