# Generated by Django 3.2.5 on 2021-08-07 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210807_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.CharField(default='00:00', max_length=12),
        ),
    ]
