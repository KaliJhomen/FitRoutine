from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Exercise, Nutrition, Manual
from .forms import ExerciseForm

def exercises_view(request, muscle_group):
    exercises = Exercise.objects.filter(muscle_group= muscle_group)
    return render(request, 'exercises.html', {'exercises': exercises, 'muscle_group': muscle_group})
def nutrition_view(request):
    nutrition = Nutrition.objects.all()
    return render(request, 'nutrition.html', {'nutrition': nutrition})

def index_view(request):
    indice = Manual.objects.all()
    return render(request, 'indice.html', {'indice': indice})
def muscle_groups_view(request):
    return render(request, 'muscle_groups.html')
@login_required
def add_exercise(request):
    if not request.user.is_superuser:
        return redirect('manual:select_muscle_group')  # Redirige si el usuario no es superusuario
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manual:select_muscle_group')
    else:
        form= ExerciseForm()
    return render(request, 'add_exercise.html', {'form': form})
