# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-30 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DraftEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=32)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('edited', models.DateTimeField(auto_now=True)),
                ('sent', models.DateTimeField(null=True)),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Sending'), (3, 'Sent')])),
            ],
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField()),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
        ),
    ]
