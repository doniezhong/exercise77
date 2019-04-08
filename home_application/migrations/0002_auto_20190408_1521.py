# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('innerip', models.CharField(max_length=50, null=True)),
                ('biz_name', models.CharField(max_length=50, null=True)),
                ('os_name', models.CharField(max_length=50, null=True)),
                ('cloud_name', models.CharField(max_length=50, null=True)),
                ('os_type', models.CharField(max_length=50, null=True)),
                ('desc', models.CharField(max_length=50, null=True)),
                ('when_created', models.CharField(max_length=50, null=True)),
                ('when_modified', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PH',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when_created', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='JobHistory',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='server',
        ),
        migrations.DeleteModel(
            name='performance',
        ),
        migrations.DeleteModel(
            name='service',
        ),
    ]
