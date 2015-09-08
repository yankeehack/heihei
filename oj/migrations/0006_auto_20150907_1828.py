# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0005_auto_20150901_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth',
            name='member_id',
            field=models.OneToOneField(to='oj.Member'),
        ),
    ]
