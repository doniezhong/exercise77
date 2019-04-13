# -*- coding: utf-8 -*-
from django.db import models


class IPConfig(models.Model):
    biz_id = models.IntegerField(null=True)
    ip = models.CharField(max_length=50)
    is_period = models.BooleanField(default=False)
    cpu = models.FloatField(null=True)
    mem = models.FloatField(null=True)
    disk = models.FloatField(null=True)


class HostPerformance(models.Model):
    biz_id = models.IntegerField()
    ip = models.CharField(max_length=50)
    cpu = models.FloatField(null=True)
    mem = models.FloatField(null=True)
    disk = models.FloatField(null=True)
    when_created = models.CharField(max_length=50, default='')
