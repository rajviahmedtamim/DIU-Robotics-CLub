# Generated by Django 3.2 on 2021-04-09 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DURCPanel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('facebook_url', models.CharField(blank=True, max_length=200, null=True)),
                ('github_url', models.CharField(blank=True, max_length=200, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=200, null=True)),
                ('linkdin_url', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='PanelMember')),
                ('details', models.TextField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='services')),
                ('details', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=30)),
                ('event_start', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('titleicle', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='services')),
                ('details', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]