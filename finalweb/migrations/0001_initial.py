# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import finalweb.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote', models.CharField(max_length=300, null=True, blank=True)),
                ('quote_author', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('complexity', models.PositiveIntegerField(default=0, null=True, blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('newest', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.CharField(max_length=1000, null=True, blank=True)),
                ('time', models.CharField(max_length=1000, null=True, blank=True)),
                ('customer', models.CharField(max_length=1000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RefImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(null=True, upload_to=finalweb.models.get_file_path, blank=True)),
                ('reference', models.ForeignKey(blank=True, to='finalweb.Reference', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
