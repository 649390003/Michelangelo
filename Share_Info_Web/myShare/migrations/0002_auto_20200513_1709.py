# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myShare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='bankcard',
            field=models.CharField(max_length=100),
        ),
    ]
