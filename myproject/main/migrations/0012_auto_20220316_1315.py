# Generated by Django 3.2.5 on 2022-03-16 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_main_insta'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='seo_keywords',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='seo_txt',
            field=models.CharField(default='-', max_length=200),
        ),
    ]