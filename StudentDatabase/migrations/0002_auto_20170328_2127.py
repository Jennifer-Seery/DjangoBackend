# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 20:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDatabase', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='trigger1',
            new_name='ColourFilter',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='trigger2',
            new_name='SoundFilter',
        ),
    ]
