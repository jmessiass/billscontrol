# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-16 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170716_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duvida',
            name='celular',
            field=models.CharField(help_text='ddd + celular', max_length=100),
        ),
    ]
