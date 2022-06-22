# Generated by Django 3.2.13 on 2022-06-22 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_property_status'),
        ('reviews', '0004_review_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='properties.property'),
        ),
    ]
