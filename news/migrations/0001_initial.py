# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=128, blank=True)),
                ('categoriya', models.TextField(max_length=200, blank=True)),
                ('image', models.TextField(max_length=500, blank=True)),
                ('images', models.TextField(max_length=5000, blank=True)),
                ('autor', models.TextField(max_length=128, blank=True)),
                ('datapost', models.DateField(null=True, blank=True)),
                ('zmist', models.TextField(max_length=10000, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
