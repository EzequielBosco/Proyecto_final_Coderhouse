# Generated by Django 4.0.3 on 2022-10-31 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('contraseña', models.CharField(max_length=20)),
            ],
        ),
    ]
