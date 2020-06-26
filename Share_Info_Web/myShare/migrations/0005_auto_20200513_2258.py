# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myShare', '0004_record'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelTable(
            name='record',
            table='actrecord',
        ),
    ]
