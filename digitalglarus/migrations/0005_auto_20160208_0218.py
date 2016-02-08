# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitalglarus', '0004_supporter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supporter',
            name='description',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
