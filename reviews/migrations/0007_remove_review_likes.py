# Generated by Django 3.2.13 on 2022-06-26 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20220623_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='likes',
        ),
    ]
