# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 12:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
