# Generated by Django 5.1.3 on 2024-12-21 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manual', '0003_muscles_tag_remove_exercise_muscle_groups_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Muscles',
            new_name='Muscle',
        ),
        migrations.RenameModel(
            old_name='NutritionalSuplements',
            new_name='NutritionalSuplement',
        ),
        migrations.RenameModel(
            old_name='Suplements',
            new_name='Suplement',
        ),
    ]
