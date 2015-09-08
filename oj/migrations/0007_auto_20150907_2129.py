# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0006_auto_20150907_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth',
            name='create',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='auth',
            name='secret',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='member',
            name='create',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
