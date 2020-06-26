# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myShare', '0008_buyorder_remark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profit',
            name='profit',
        ),
        migrations.RemoveField(
            model_name='profit',
            name='totalvalue',
        ),
        migrations.AddField(
            model_name='sellorder',
            name='remark',
            field=models.CharField(max_length=100, default=0),
            preserve_default=False,
        ),
    ]
