# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-24 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190724_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=18),
        ),
    ]
