# Generated by Django 5.1.3 on 2024-12-24 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_userprofile_biceps_remove_userprofile_chest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodymeasurement',
            name='biceps',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurement',
            name='chest',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurement',
            name='forearm',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurement',
            name='glutes',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurement',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurement',
            name='shoulders',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurement',
            name='waist',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bodymeasurement',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]