from django.db import models
from django.conf import settings
from manual.models import Exercise
class WorkoutRoutine(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']  # Keep the latest routines first

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(WorkoutRoutine, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.FloatField(null=True, blank=True)  # Optional field for weight used

    def __str__(self):
        return f"{self.workout.name} - {self.exercise.name}"