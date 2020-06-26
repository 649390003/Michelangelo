# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myShare', '0006_sharedailyinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharedailyinfo',
            name='date',
        ),
        migrations.AddField(
            model_name='sharedailyinfo',
            name='infotimes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
