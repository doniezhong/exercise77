# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_auto_20190408_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='biz_id',
            field=models.CharField(default=b'', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='host',
            name='set_id',
            field=models.CharField(default=b'', max_length=50, null=True),
        ),
    ]
