# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raffle', '0003_raffle_results'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raffle',
            name='winner',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]