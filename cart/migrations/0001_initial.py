# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('goods_num', models.IntegerField()),
                ('goods_info', models.ForeignKey(to='goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('order_id', models.CharField(max_length=100)),
                ('order_addr', models.CharField(max_length=100)),
                ('order_recv', models.CharField(max_length=50)),
                ('order_tele', models.CharField(max_length=11)),
                ('order_fee', models.IntegerField(default=10)),
                ('order_extra', models.CharField(max_length=200)),
                ('order_status', models.IntegerField(default=1, choices=[(1, '待付款'), (2, '待发货'), (3, '待收货'), (4, '已完成')])),
            ],
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='goods_order',
            field=models.ForeignKey(to='cart.OrderInfo'),
        ),
    ]
