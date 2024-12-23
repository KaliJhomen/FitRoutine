# Generated by Django 5.1.3 on 2024-12-23 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manual', '0005_exercise_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutritionalsuplement',
            name='description',
        ),
        migrations.RemoveField(
            model_name='nutritionalsuplement',
            name='nutritional_suplements',
        ),
        migrations.AddField(
            model_name='suplement',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='suplement',
            name='nutritional_suplement',
            field=models.ManyToManyField(to='manual.nutritionalsuplement'),
        ),
        migrations.AlterField(
            model_name='nutritionalsuplement',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='suplement',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
