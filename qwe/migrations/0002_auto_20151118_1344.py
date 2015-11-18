# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qwe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foo',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
