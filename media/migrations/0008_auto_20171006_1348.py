# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0007_auto_20171006_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='featured_image',
            field=models.URLField(max_length=500),
        ),
    ]
