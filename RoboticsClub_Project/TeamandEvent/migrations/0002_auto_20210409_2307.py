# Generated by Django 3.2 on 2021-04-09 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamandEvent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_start',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
