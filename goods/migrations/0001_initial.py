# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cag_name', models.CharField(max_length=30)),
                ('cag_css', models.CharField(max_length=20)),
                ('cag_img', models.ImageField(upload_to='cag')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('goods_name', models.CharField(max_length=100)),
                ('goods_unit', models.CharField(max_length=50)),
                ('goods_price', models.IntegerField(default=0)),
                ('goods_img', models.ImageField(upload_to='goods')),
                ('goods_desc', models.CharField(max_length=2000)),
                ('goods_cag', models.ForeignKey(to='goods.GoodsCategory')),
            ],
        ),
    ]
