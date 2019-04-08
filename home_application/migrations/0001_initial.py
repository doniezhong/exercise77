# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobHistory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True)),
                ('bk_biz_id', models.IntegerField(null=True, verbose_name='\u4e1a\u52a1ID')),
                ('bk_biz_name', models.CharField(max_length=50, null=True, verbose_name='\u4e1a\u52a1\u540d\u79f0')),
                ('bk_job_id', models.IntegerField(null=True, verbose_name='job_id')),
                ('bk_instance_id', models.IntegerField(null=True, verbose_name='instance_id')),
                ('start_time', models.DateTimeField(null=True, verbose_name='\u64cd\u4f5c\u8005')),
                ('operator', models.CharField(max_length=50, null=True, verbose_name='\u64cd\u4f5c\u8005')),
                ('ip_list', models.CharField(max_length=2500, null=True, verbose_name='ip\u5217\u8868')),
                ('status', models.CharField(max_length=50, null=True, verbose_name='\u4f5c\u4e1a\u72b6\u6001')),
                ('log_content', models.CharField(max_length=250, null=True, verbose_name='\u4f5c\u4e1a\u65e5\u5fd7')),
            ],
        ),
        migrations.CreateModel(
            name='performance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpu', models.FloatField()),
                ('disk', models.FloatField()),
                ('men', models.FloatField()),
                ('created', models.DateTimeField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_address', models.CharField(max_length=50, null=True, verbose_name='ip\u5730\u5740')),
                ('ip_name', models.CharField(max_length=100, null=True, verbose_name='\u4e3b\u673a\u540d\u79f0')),
                ('cloud_id', models.IntegerField(null=True, verbose_name='\u4e91\u533a\u57dfid')),
                ('app_id', models.IntegerField(null=True, verbose_name='\u4e1a\u52a1id')),
            ],
        ),
        migrations.AddField(
            model_name='performance',
            name='server',
            field=models.ForeignKey(to='home_application.service'),
        ),
    ]
