# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-04-30 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0029_userhostingkey_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='userhostingkey',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
