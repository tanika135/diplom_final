# Generated by Django 4.2.1 on 2023-06-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0004_order_created_order_email_order_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
