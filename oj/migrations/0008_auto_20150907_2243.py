# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0007_auto_20150907_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auth',
            old_name='member_id',
            new_name='member',
        ),
    ]
