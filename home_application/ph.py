# -*- coding: utf-8 -*-
from conf.default import APP_TOKEN, APP_ID
from blueking.component.shortcuts import ComponentClient
from utilities.jobman import JobMan
from utilities.utils import *
from home_application.models import PH

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


def execute_job():
    hosts = search_cc_host()
    job = JobMan()
    ph_list = []
    for host in hosts:
        try:
            app_id = host['biz'][0]['bk_biz_id']
            ip = host['host']['bk_host_innerip']
            host_list = [
                {
                    'ip': host['host']['bk_host_innerip'],
                    'bk_cloud_id': host['host']['bk_cloud_id'][0]['bk_inst_id']
                }
            ]
            job_obj = {
                app_id: [
                    {
                        "host": host_list,
                        "script_content": "cat /proc/loadavg",
                        "script_type": "1",
                        "account": "root"
                    }
                ]
            }
            job.execute(job_obj)
            _, content = job.get_log(ip)
            ph = content.split(' ')[1]
            ph_obj = {
                'ip': ip,
                'cpu': ph,
                'when_created': get_time_now_str()
            }
            ph_list.append(ph_obj)
        except Exception as e:
            print e
    for p in ph_list:
        PH.objects.create(**p)

