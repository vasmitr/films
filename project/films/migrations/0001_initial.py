# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rating', models.IntegerField(choices=[(0, 'Нет оценки'), (1, 'Плохо'), (2, 'Сойдет'), (3, 'Средне'), (4, 'Неплохо'), (5, 'Круто')], default=0)),
                ('image', models.ImageField(upload_to='')),
                ('base_price', models.IntegerField()),
                ('relise_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'ordering': ['rating'],
            },
        ),
    ]
