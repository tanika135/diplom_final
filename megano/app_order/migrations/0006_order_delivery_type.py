# Generated by Django 4.2.1 on 2023-06-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0005_order_address_order_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(choices=[('FR', 'free'), ('PA', 'paid')], default='FR', max_length=2),
        ),
    ]