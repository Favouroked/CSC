# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-07-18 02:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cscapp', '0003_auto_20170718_0130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('url', models.URLField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cscapp.Course')),
            ],
        ),
        migrations.AlterField(
            model_name='textbook',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
