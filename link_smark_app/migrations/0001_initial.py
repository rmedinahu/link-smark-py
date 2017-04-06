# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bkmark_title', models.CharField(max_length=255)),
                ('bkmark_address', models.URLField(max_length=255)),
                ('bkmark_date', models.DateTimeField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr_post', models.URLField(max_length=255)),
                ('usr_post_msg', models.CharField(max_length=255)),
                ('post_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_keywrd', models.CharField(max_length=255)),
                ('tag_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usr_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('interests', models.CharField(max_length=255)),
            ],
        ),
    ]