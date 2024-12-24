from django.db import models
from django.conf import settings
from manual.models import Exercise, Muscle
class WorkoutRoutine(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']  

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class WorkoutExercise(models.Model):
    workout_routine = models.ForeignKey(WorkoutRoutine, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField(null=True, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)  

    def __str__(self):
        return f"{self.workout_routine.name} - {self.exercise.name}"