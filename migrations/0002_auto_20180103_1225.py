# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-03 12:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Person_Group'),
        ),
    ]
