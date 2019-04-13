# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_hostperformance_when_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipconfig',
            name='biz_id',
            field=models.IntegerField(null=True),
        ),
    ]
