# Generated by Django 4.1.2 on 2022-10-28 13:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0004_match_sports'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='session_year',
        ),
        migrations.CreateModel(
            name='MatchDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('match_date', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('session_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.session')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='match_date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matches.matchdate'),
        ),
    ]
