# Generated by Django 4.0.3 on 2022-11-11 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_remove_comentario_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
