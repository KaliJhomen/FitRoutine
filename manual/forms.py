from django import forms
from .models import Exercise, Nutrition, Encyclopedia

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'muscle_group', 'image']

class NutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        fields = ['title', 'content', 'image']

class EncyclopediaForm(forms.ModelForm):
    class Meta:
        model = Encyclopedia
        fields = ['question', 'answer']