# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('favoritedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formv.User')),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotedby', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=140)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('postedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formv.User')),
            ],
        ),
        migrations.AddField(
            model_name='favorite',
            name='favoritequote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.Quote'),
        ),
    ]