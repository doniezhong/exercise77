# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostPerformance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('biz_id', models.IntegerField()),
                ('ip', models.CharField(max_length=50)),
                ('cpu', models.FloatField()),
                ('mem', models.FloatField()),
                ('disk', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='IPConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('biz_id', models.IntegerField()),
                ('ip', models.CharField(max_length=50)),
                ('is_period', models.BooleanField(default=True)),
            ],
        ),
    ]
