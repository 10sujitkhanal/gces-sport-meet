# Generated by Django 4.1.2 on 2022-10-30 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sports',
            name='sport_type',
            field=models.CharField(choices=[('MULTIPLE', 'MULTIPLE'), ('SINGLE', 'SINGLE')], default='MULTIPLE', max_length=9),
        ),
    ]
