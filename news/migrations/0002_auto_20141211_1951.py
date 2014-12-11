# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 17, 51, 56, 852000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
