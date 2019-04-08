# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0005_ph_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ph',
            name='cpu',
            field=models.FloatField(default=0),
        ),
    ]
