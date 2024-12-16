from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description', 'muscle_group', 'exercises', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
        }

class WorkoutEditForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description', 'muscle_group', 'exercises', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
        }