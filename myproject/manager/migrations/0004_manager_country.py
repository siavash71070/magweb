# Generated by Django 3.2.5 on 2021-08-28 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_manager_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='country',
            field=models.TextField(default=''),
        ),
    ]