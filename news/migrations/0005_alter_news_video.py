# Generated by Django 4.1.2 on 2022-10-30 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news_post_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='video',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
