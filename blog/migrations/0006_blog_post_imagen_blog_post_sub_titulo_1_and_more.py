# Generated by Django 4.0.3 on 2022-10-31 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='imagen',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog_post',
            name='sub_titulo_1',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog_post',
            name='cuerpo',
            field=models.CharField(max_length=400),
        ),
    ]