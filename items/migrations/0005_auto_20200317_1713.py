# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-17 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20200310_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('s', 'Small'), ('m', 'Medium'), ('l', 'Large')], max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='features',
            field=models.CharField(default='some features', max_length=240),
        ),
        migrations.RemoveField(
            model_name='item',
            name='sizes',
        ),
        migrations.AddField(
            model_name='itemsize',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item'),
        ),
        migrations.AddField(
            model_name='itemsize',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Size'),
        ),
        migrations.AddField(
            model_name='item',
            name='sizes',
            field=models.ManyToManyField(related_name='sizes', through='items.ItemSize', to='items.Size'),
        ),
    ]
