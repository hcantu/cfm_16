# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ano_escolar', '0002_auto_20160106_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='anuario',
        ),
    ]
