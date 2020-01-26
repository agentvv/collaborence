# Generated by Django 3.0.2 on 2020-01-26 07:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='time',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='time',
        ),
        migrations.AddField(
            model_name='comment',
            name='timeCreated',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='reply',
            name='timeCreated',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
