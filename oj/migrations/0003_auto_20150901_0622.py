# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0002_auto_20150827_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(default=b'', max_length=254),
        ),
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='member',
            name='username',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
