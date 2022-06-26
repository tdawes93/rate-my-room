# Generated by Django 3.2.13 on 2022-06-26 20:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('properties', '0007_auto_20220625_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='property_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
