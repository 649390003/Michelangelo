# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myShare', '0002_auto_20200513_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='bankcard',
            field=models.CharField(max_length=20),
        ),
    ]
