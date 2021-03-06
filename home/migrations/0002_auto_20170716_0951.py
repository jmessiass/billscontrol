# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-16 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name': 'Home', 'verbose_name_plural': 'Home'},
        ),
        migrations.RenameField(
            model_name='home',
            old_name='texto_principal',
            new_name='texto_primario',
        ),
        migrations.AlterField(
            model_name='home',
            name='imagem',
            field=models.ImageField(blank=True, help_text='Aceita qualquer imagem sem espaço e caracteres especiais.<br>Tamanho recomendado 400x362.', null=True, upload_to='home/'),
        ),
    ]
