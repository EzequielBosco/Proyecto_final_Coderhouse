# Generated by Django 4.0.3 on 2022-11-04 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_rename_configuracion1_configuracionblog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ConfiguracionBlog',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='desarrollado_por',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='nombre_blog',
        ),
    ]
