# Generated by Django 4.2.1 on 2023-06-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0009_alter_order_payment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(choices=[('ORD', 'ordinary'), ('EXP', 'express')], default='ORD', max_length=4),
        ),
    ]
