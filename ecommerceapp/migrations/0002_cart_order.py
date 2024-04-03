# Generated by Django 5.0.1 on 2024-03-19 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('quantity', models.IntegerField()),
                ('cart_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('quantity', models.IntegerField()),
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.user')),
            ],
        ),
    ]
