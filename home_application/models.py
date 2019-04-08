# -*- coding: utf-8 -*-
from django.db import models


class Host(models.Model):
    innerip = models.CharField(max_length=50, null=True)
    biz_name = models.CharField(max_length=50, null=True)
    biz_id = models.CharField(max_length=50, null=True, default='')
    set_id = models.CharField(max_length=50, null=True, default='')
    os_name = models.CharField(max_length=50, null=True)
    cloud_name = models.CharField(max_length=50, null=True)
    os_type = models.CharField(max_length=50, null=True)
    desc = models.CharField(max_length=50, null=True)
    when_created = models.CharField(max_length=50, null=True)
    when_modified = models.CharField(max_length=50, null=True)

class PH(models.Model):
    when_created = models.CharField(max_length=50)
    cpu = models.FloatField(default=0)
    ip = models.CharField(max_length=50, default='')

