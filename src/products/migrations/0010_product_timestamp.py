# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-02 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20190501_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
