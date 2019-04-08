# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0004_ph_cpu'),
    ]

    operations = [
        migrations.AddField(
            model_name='ph',
            name='ip',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
