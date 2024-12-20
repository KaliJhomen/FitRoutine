from django import forms
from .models import Exercise, Nutrition, Manual

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'muscle_group', 'image', 'video']

class NutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        fields = ['title', 'content', 'image']

class ManualForm(forms.ModelForm):
    class Meta:
        model = Manual
        fields = ['question', 'answer']