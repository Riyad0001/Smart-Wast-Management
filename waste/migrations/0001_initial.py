# Generated by Django 5.1.5 on 2025-01-27 17:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WasteBin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('capacity', models.IntegerField()),
                ('current_fill', models.IntegerField()),
                ('last_collected', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waste.wastebin')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_time', models.DateTimeField()),
                ('bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waste.wastebin')),
            ],
        ),
    ]
