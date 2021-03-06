# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-01 07:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0005_auto_20170101_0036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight_info',
            old_name='departing_time',
            new_name='departing_arrival_time',
        ),
        migrations.RenameField(
            model_name='flight_info',
            old_name='return_time',
            new_name='departing_departing_time',
        ),
        migrations.AddField(
            model_name='flight_info',
            name='return_arrival_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 1, 1, 40, 5, 290802)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight_info',
            name='return_departing_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 1, 1, 40, 14, 196136)),
            preserve_default=False,
        ),
    ]
