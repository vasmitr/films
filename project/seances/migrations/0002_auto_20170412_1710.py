# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 17:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seances', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='day',
            options={'ordering': ['number'], 'verbose_name': 'День недели', 'verbose_name_plural': 'Дни недели'},
        ),
        migrations.AlterModelOptions(
            name='seance',
            options={'ordering': ['day', 'start', 'end'], 'verbose_name': 'Время сеанса', 'verbose_name_plural': 'Время сеанса'},
        ),
    ]
