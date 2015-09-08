# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('website', models.CharField(default=b'', max_length=200)),
                ('tagline', models.CharField(default=b'', max_length=200)),
                ('bio', models.CharField(default=b'', max_length=200)),
                ('gravatar_link', models.CharField(default=b'', max_length=200)),
                ('admin', models.IntegerField(default=0)),
                ('lang', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='auth',
            name='member_id',
            field=models.ForeignKey(to='oj.Member'),
        ),
    ]
