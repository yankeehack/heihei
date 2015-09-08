# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0004_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
