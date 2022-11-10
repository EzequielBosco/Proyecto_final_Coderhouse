# Generated by Django 4.0.3 on 2022-11-10 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('sub_titulo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ConfigContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('sub_titulo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ConfigIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('sub_titulo', models.CharField(max_length=30)),
                ('sub_titulo_1', models.CharField(max_length=30)),
            ],
        ),
    ]
