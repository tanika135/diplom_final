# Generated by Django 4.2.1 on 2023-05-29 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0010_alter_profile_avatar'),
        ('app_catalog', '0012_productreviews_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreviews',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='app_auth.profile'),
            preserve_default=False,
        ),
    ]
