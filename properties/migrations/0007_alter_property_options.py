# Generated by Django 3.2.13 on 2022-06-20 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_auto_20220619_1614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['-created_on', 'title'], 'verbose_name_plural': 'Properties'},
        ),
    ]
