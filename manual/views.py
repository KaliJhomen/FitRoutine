from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Exercise, NutritionalSuplements, Manual, MuscleGroup


def muscle_groups_view(request):
    muscle_groups = MuscleGroup.objects.all()
    return render(request, 'muscle_groups.html', {'muscle_groups': muscle_groups})

def exercises_view(request, muscle_group_name):
    muscle_group = get_object_or_404(MuscleGroup, name=muscle_group_name)
    exercises = Exercise.objects.filter(muscle_groups= muscle_group)
    return render(request, 'exercises.html', {'exercises': exercises, 'muscle_groups': muscle_group.name})

def nutritional_suplements_view(request):
    nutrition = NutritionalSuplements.objects.all()
    return render(request, 'nutritional_suplements.html', {'nutrition': nutrition})

def index_view(request):
    indice = Manual.objects.all()
    return render(request, 'indice.html', {'indice': indice})





