# Generated by Django 4.0.3 on 2022-11-07 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_remove_configbase_sub_titulo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configbase',
            name='link_github',
        ),
    ]