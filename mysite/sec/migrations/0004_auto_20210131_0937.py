# Generated by Django 3.1.5 on 2021-01-31 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sec', '0003_auto_20210131_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchobj',
            name='user_one_consensus',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='matchobj',
            name='user_two_consensus',
            field=models.CharField(blank=True, max_length=6),
        ),
    ]
