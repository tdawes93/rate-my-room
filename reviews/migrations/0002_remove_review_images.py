# Generated by Django 3.2.13 on 2022-06-28 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='images',
        ),
    ]
