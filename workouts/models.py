from django.db import models
from django.contrib.auth.models import User
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='exercises/', blank=True)
    muscle_group = models.CharField(max_length=50)

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    muscle_group = models.CharField(max_length=50)
    exercises = models.ManyToManyField(Exercise)
    image = models.ImageField(upload_to='workouts/', blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserBodyMetrics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    shoulder_measurement = models.FloatField()
    chest_measurement = models.FloatField()
    waist_measurement = models.FloatField()
    bicep_measurement = models.FloatField()
    forearm_measurement = models.FloatField()
    glute_measurement = models.FloatField()
    date_recorded = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_recorded']  # Keep the latest measurements first

    def __str__(self):
        return f"{self.user.username} - {self.date_recorded}"