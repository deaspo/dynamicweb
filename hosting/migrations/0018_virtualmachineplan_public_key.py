# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-24 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0017_virtualmachinetype_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualmachineplan',
            name='public_key',
            field=models.TextField(default='sada'),
            preserve_default=False,
        ),
    ]
