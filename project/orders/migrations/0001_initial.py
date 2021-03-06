# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 17:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seances', '0002_auto_20170412_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('row_markup', models.FloatField(default=0.0)),
                ('reserved', models.BooleanField(default=False)),
                ('seance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seances.Seance')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('seance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seances.Seance')),
                ('seat', models.ManyToManyField(to='orders.Seat')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
            },
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together=set([('number', 'seance')]),
        ),
    ]
