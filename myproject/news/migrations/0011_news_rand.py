# Generated by Django 3.2.5 on 2021-08-26 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_news_act'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='rand',
            field=models.IntegerField(default=0),
        ),
    ]
