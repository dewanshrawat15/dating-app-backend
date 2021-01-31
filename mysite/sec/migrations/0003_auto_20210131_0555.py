# Generated by Django 3.1.5 on 2021-01-31 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sec', '0002_matchobj'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchobj',
            name='user_one_consensus',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='matchobj',
            name='user_two_consensus',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]