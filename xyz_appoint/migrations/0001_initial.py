# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2022-05-08 23:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import xyz_util.modelutils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=32, unique=True, verbose_name='\u6807\u8bc6')),
                ('session_max_age', models.CharField(blank=True, default='7d', max_length=16, verbose_name='\u5355\u6b21\u8fc7\u671f\u65f6\u95f4')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u6709\u6548')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6388\u6743',
                'verbose_name_plural': '\u6388\u6743',
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=32, unique=True, verbose_name='\u6807\u8bc6')),
                ('name', models.CharField(blank=True, default='', max_length=64, verbose_name='\u540d\u79f0')),
                ('scope', xyz_util.modelutils.JSONField(blank=True, default={}, verbose_name='\u8303\u56f4')),
                ('context', xyz_util.modelutils.JSONField(blank=True, default={}, verbose_name='\u4e0a\u4e0b\u6587')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u6709\u6548')),
                ('expire_time', models.DateTimeField(blank=True, null=True, verbose_name='\u8fc7\u671f\u65f6\u95f4')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7ea6\u5b9a',
                'verbose_name_plural': '\u7ea6\u5b9a',
            },
        ),
        migrations.AddField(
            model_name='appointment',
            name='policy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appoint.Policy', verbose_name='\u7ea6\u5b9a'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='appoint_appointments', to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237'),
        ),
    ]
