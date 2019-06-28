# -*- coding: utf-8 -*-
from datetime import datetime


def datetime_to_str(datetime, format="%Y-%m-%d %H:%M:%S"):
    return datetime.strftime(format)


def utc_to_datetime(time_str):
    return datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%fZ')


def now_time():
    now = datetime.now()
    return now


def now_time_str():
    return datetime_to_str(now_time())
