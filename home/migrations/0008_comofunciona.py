# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-17 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170716_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComoFunciona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('imagem', models.ImageField(blank=True, help_text='Formatos recomendado: JPG e PNG.', null=True, upload_to='home/')),
                ('texto', models.TextField(max_length=255)),
                ('ativo', models.BooleanField(default=1)),
            ],
        ),
    ]
