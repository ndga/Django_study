# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-29 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=18, verbose_name='用户名')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户列表',
                'verbose_name_plural': '用户列表',
            },
        ),
    ]
