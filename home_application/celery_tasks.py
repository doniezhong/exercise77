# -*- coding: utf-8 -*-
"""
celery 任务示例

本地启动celery命令: python  manage.py  celery  worker  --settings=settings
周期性任务还需要启动celery调度命令：python  manage.py  celerybeat --settings=settings
"""
from celery.schedules import crontab
from celery.task import periodic_task
from home_application.ph import execute_job


@periodic_task(run_every=crontab(minute='*/5', hour='*', day_of_week="*"))
def performance():
    execute_job()
