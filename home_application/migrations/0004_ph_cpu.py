# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0003_auto_20190408_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='ph',
            name='cpu',
            field=models.IntegerField(default=0),
        ),
    ]
