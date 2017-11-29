# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-29 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='definition',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='example',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
