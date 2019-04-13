# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0004_auto_20190413_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipconfig',
            name='is_period',
            field=models.BooleanField(default=False),
        ),
    ]
