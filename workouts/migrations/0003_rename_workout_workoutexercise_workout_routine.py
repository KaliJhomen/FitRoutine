# Generated by Django 5.1.3 on 2024-12-24 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_alter_workoutexercise_reps_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workoutexercise',
            old_name='workout',
            new_name='workout_routine',
        ),
    ]