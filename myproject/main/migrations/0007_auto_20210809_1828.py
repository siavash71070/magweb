# Generated by Django 3.2.5 on 2021-08-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210727_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='picname',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='main',
            name='picurl',
            field=models.TextField(default=''),
        ),
    ]