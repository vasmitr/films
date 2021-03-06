# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('weekend', models.BooleanField(default=False)),
                ('weekend_markup', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name': 'День недели',
                'verbose_name_plural': 'Дни недели',
            },
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('time_markup', models.FloatField(default=0.0)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seances.Day')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.Film')),
            ],
            options={
                'verbose_name': 'Время сеанса',
                'verbose_name_plural': 'Время сеанса',
                'ordering': ['start', 'end'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='seance',
            unique_together=set([('start', 'end', 'day')]),
        ),
    ]
