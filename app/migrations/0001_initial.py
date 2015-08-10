# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('publication_date', models.DateField()),
                ('publisher', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('link', models.URLField(max_length=1024)),
                ('cover_image', models.ImageField(upload_to='')),
                ('author', models.ManyToManyField(to='app.Author')),
            ],
        ),
    ]
