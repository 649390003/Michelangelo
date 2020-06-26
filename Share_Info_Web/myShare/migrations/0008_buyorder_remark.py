# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myShare', '0007_auto_20200515_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyorder',
            name='remark',
            field=models.CharField(max_length=100, default=0),
            preserve_default=False,
        ),
    ]
