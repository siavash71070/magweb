# Generated by Django 3.2.5 on 2021-08-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcat', '0002_rename_cat_subcat'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcat',
            name='catid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subcat',
            name='catname',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
