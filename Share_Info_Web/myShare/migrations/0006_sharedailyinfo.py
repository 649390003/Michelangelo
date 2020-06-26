# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myShare', '0005_auto_20200513_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareDailyInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('highestp', models.FloatField()),
                ('lowestp', models.FloatField()),
                ('startp', models.FloatField()),
                ('closep', models.FloatField()),
                ('date', models.DateField()),
                ('share', models.ForeignKey(to='myShare.Shares')),
            ],
            options={
                'db_table': 'sharedailyinfo',
                'ordering': ['id'],
            },
        ),
    ]
