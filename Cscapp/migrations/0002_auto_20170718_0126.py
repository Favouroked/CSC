# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-07-18 01:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cscapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
        migrations.RenameModel(
            old_name='Textbooks',
            new_name='Textbook',
        ),
    ]
