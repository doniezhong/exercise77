# -*- coding: utf-8 -*-
import time
from datetime import datetime, timedelta


def datetime_to_str(datetime, format="%Y-%m-%d %H:%M:%S"):
    return datetime.strftime(format)


def utc_to_datetime(time_str):
    return datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%fZ')


def now_time():
    now = datetime.now()
    return now


def now_time_str():
    return datetime_to_str(now_time())


def utc_to_local(utc_st):
    '''UTC时间转本地时间（+8:00）'''
    now_stamp = time.time()
    local_time = datetime.fromtimestamp(now_stamp)
    utc_time = datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st


def local_to_utc(local_st):
    '''本地时间转UTC时间（-8:00）'''
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.utcfromtimestamp(time_struct)
    return utc_st


def time_loads(str):
    # utc字符串直接转化为当地时间的datetime
    utc_st = utc_to_datetime(str)
    return utc_to_local(utc_st)


def time_operation(dtime, ):
    timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)