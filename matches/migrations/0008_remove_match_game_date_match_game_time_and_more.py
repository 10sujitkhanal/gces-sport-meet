# Generated by Django 4.1.2 on 2022-10-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_remove_match_organizer_matchdate_organizer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='game_date',
        ),
        migrations.AddField(
            model_name='match',
            name='game_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='singlematch',
            name='game_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
