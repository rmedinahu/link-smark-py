# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('link_smark_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmarkcomments',
            name='bookmark',
        ),
        migrations.RemoveField(
            model_name='bookmarkcomments',
            name='post',
        ),
        migrations.AddField(
            model_name='posts',
            name='bookmark',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='link_smark_app.Bookmarks'),
        ),
        migrations.AlterField(
            model_name='taggedbookmark',
            name='bookmark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='link_smark_app.Bookmarks'),
        ),
        migrations.DeleteModel(
            name='BookmarkComments',
        ),
    ]