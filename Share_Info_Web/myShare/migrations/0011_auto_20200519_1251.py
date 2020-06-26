# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myShare', '0010_auto_20200517_2126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'ordering': ['rdate']},
        ),
    ]
