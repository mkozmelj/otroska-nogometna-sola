# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obvestila', '0002_auto_20170103_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='trener',
            name='slika',
            field=models.ImageField(default='/static/obvestila/img/contact.png', upload_to=''),
        ),
    ]