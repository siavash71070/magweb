# Generated by Django 3.2.5 on 2021-08-07 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210804_2156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='pic',
            new_name='picname',
        ),
        migrations.AddField(
            model_name='news',
            name='picurl',
            field=models.TextField(default='-'),
        ),
    ]