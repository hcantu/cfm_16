# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=20)),
                ('exe', models.BooleanField(unique=True, max_length=15)),
                ('prim10', models.CharField(max_length=15)),
                ('foto_gde', models.CharField(max_length=15)),
                ('foto_med', models.CharField(max_length=15)),
                ('foto_peq', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Anuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anuario', models.CharField(unique=True, max_length=10)),
                ('anuario_text', models.CharField(unique=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Salones_curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('salon', models.CharField(unique=True, max_length=10)),
                ('curso', models.CharField(unique=True, max_length=15)),
                ('anuario', models.ForeignKey(to='ano_escolar.Anuario')),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='anuario',
            field=models.ForeignKey(to='ano_escolar.Anuario'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='salon',
            field=models.ForeignKey(to='ano_escolar.Salones_curso'),
        ),
    ]
