# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent_id',
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/images/covers/', verbose_name='Book cover picture'),
        ),
    ]
