# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0011_auto_20170131_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.Organisation'),
        ),
    ]