from django import forms
from .models import WorkoutRoutine, WorkoutExercise

class WorkoutRoutineForm(forms.ModelForm):
    class Meta:
        model = WorkoutRoutine
        fields = ['name', 'exercises']
        widgets = {
            'exercises': forms.CheckboxSelectMultiple(),
        }

class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps', 'weight']