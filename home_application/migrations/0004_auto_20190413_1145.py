# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0003_auto_20190413_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipconfig',
            name='cpu',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='ipconfig',
            name='disk',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='ipconfig',
            name='mem',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='hostperformance',
            name='cpu',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='hostperformance',
            name='disk',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='hostperformance',
            name='mem',
            field=models.FloatField(null=True),
        ),
    ]
