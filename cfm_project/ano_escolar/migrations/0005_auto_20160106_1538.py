# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ano_escolar', '0004_auto_20160106_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='foto_gde',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='foto_med',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='foto_peq',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
