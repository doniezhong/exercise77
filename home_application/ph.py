# -*- coding: utf-8 -*-
from conf.default import APP_TOKEN, APP_ID
from blueking.component.shortcuts import ComponentClient
from utilities.jobman import JobMan
from utilities.utils import *
from home_application.models import IPConfig, HostPerformance


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
    return_data = []
    for x in res['data']['info']:
        ip = x['host']['bk_host_innerip']
        conf = IPConfig.objects.filter(ip=ip, is_period=True)
        if not len(conf):
            continue
        return_data.append(x)
    return return_data


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
            ph_obj = {
                'ip': ip,
                'biz_id': app_id,
                'cpu': float(s_list[3].strip('\n').strip('%')),
                'mem': float(s_list[1].strip('\n').strip('%')),
                'disk': float(s_list[2].strip('\n').strip('%')),
                'when_created': get_time_now_str()
            }
            ph_list.append(ph_obj)
        except Exception as e:
            print e
        for x in ph_list:
            HostPerformance.objects.create(**x)
