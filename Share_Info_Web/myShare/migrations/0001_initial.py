# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('bankcard', models.CharField(max_length=20)),
                ('paypassword', models.CharField(max_length=20)),
                ('balance', models.FloatField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'account',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='BuyOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('expectprice', models.FloatField()),
                ('buynum', models.IntegerField()),
                ('isSuccess', models.BooleanField(default=False)),
                ('ordertime', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'buyorder',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ColsingPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sclose', models.FloatField()),
                ('sdate', models.DateField()),
                ('smonth', models.IntegerField()),
                ('sweek', models.IntegerField()),
                ('sweekday', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'colsing_price',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('buyrate', models.FloatField()),
                ('nowrate', models.FloatField()),
                ('sharenum', models.IntegerField()),
                ('totalvalue', models.FloatField()),
                ('profit', models.FloatField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profit',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SellOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('expectprice', models.FloatField()),
                ('sellnum', models.IntegerField()),
                ('isSuccess', models.BooleanField(default=False)),
                ('ordertime', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sellorder',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Shares',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sname', models.CharField(max_length=20)),
                ('snumber', models.CharField(max_length=10)),
                ('issuenum', models.IntegerField()),
                ('issuedate', models.DateTimeField(auto_now_add=True)),
                ('hprice', models.FloatField()),
                ('lprice', models.FloatField()),
                ('nprice', models.FloatField()),
                ('isDelete', models.BooleanField(default=False)),
                ('owner', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'shares',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('onlinename', models.CharField(max_length=20)),
                ('gender', models.BooleanField(default=False)),
                ('mobilephone', models.CharField(max_length=15)),
                ('uploadimg', models.ImageField(default='media/myShare/profile_small.jpg', upload_to='myShare')),
                ('isDelete', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'userinfo',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='sellorder',
            name='share',
            field=models.ForeignKey(to='myShare.Shares'),
        ),
        migrations.AddField(
            model_name='profit',
            name='share',
            field=models.ForeignKey(to='myShare.Shares'),
        ),
        migrations.AddField(
            model_name='buyorder',
            name='share',
            field=models.ForeignKey(to='myShare.Shares'),
        ),
    ]
