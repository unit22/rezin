# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 20:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mi', '0002_remove_category3_cat1'),
    ]

    operations = [
        migrations.AddField(
            model_name='category3',
            name='cat1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mi.Category1'),
        ),
        migrations.AddField(
            model_name='item',
            name='cat1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mi.Category1'),
        ),
        migrations.AddField(
            model_name='item',
            name='cat2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mi.Category2'),
        ),
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='category2',
            name='cat1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mi.Category1'),
        ),
        migrations.AlterField(
            model_name='category3',
            name='cat2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mi.Category2'),
        ),
        migrations.AlterField(
            model_name='item',
            name='cat3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mi.Category3'),
        ),
    ]
