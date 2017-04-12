# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_auto_20170412_1433'),
        ('orders', '0002_auto_20170412_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='film',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='films.Film'),
            preserve_default=False,
        ),
    ]