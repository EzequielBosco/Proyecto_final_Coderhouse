# Generated by Django 4.0.3 on 2022-11-07 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0003_rename_perfil_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Perfil',
        ),
    ]