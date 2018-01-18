# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-17 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_facetrack_status_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facetrack',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.Person_Group'),
        ),
    ]
