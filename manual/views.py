from django.shortcuts import render
from .models import Exercise, Nutrition, Encyclopedia

def exercises_view(request):
    exercise = Exercise.objects.all()
    return render(request, 'manual/exercises.html', {'exercises': exercise})

def nutrition_view(request):
    nutrition = Nutrition.objects.all()
    return render(request, 'manual/nutrition.html', {'nutrition': nutrition})

def encyclopedia_view(request):
    encyclopedia = Encyclopedia.objects.all()
    return render(request, 'manual/encyclopedia.html', {'encyclopedia': encyclopedia})