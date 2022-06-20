# Generated by Django 3.2.13 on 2022-06-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_rename_address_street_property_street_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='address_country',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='property',
            name='address_street2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Address Line 2'),
        ),
        migrations.AlterField(
            model_name='property',
            name='address_town',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Town'),
        ),
        migrations.AlterField(
            model_name='property',
            name='street_address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Address Line 1'),
        ),
    ]
