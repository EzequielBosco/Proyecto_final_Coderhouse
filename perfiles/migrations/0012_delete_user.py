# Generated by Django 4.0.3 on 2022-11-08 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0011_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]