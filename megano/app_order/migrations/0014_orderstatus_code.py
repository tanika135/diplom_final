# Generated by Django 4.2.1 on 2023-06-05 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0013_orderstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstatus',
            name='code',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
