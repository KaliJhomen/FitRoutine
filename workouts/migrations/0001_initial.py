# Generated by Django 5.1.3 on 2024-12-18 21:40

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
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='exercises/')),
                ('muscle_group', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserBodyMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('shoulder_measurement', models.FloatField()),
                ('chest_measurement', models.FloatField()),
                ('waist_measurement', models.FloatField()),
                ('bicep_measurement', models.FloatField()),
                ('forearm_measurement', models.FloatField()),
                ('glute_measurement', models.FloatField()),
                ('date_recorded', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_recorded'],
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('muscle_group', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='workouts/')),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('exercises', models.ManyToManyField(to='workouts.exercise')),
            ],
        ),
    ]
