# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-07-31 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
