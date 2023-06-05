# Generated by Django 4.2.1 on 2023-06-05 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0011_orderitems_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
