from django.shortcuts import render, get_object_or_404
from .models import Exercise, NutritionalSuplement, Suplement, Manual, Muscle


def muscles_view(request):
    muscles = Muscle.objects.all()
    return render(request, 'muscles.html', {'muscles': muscles})

def exercises_view(request, muscle_name):
    muscle = get_object_or_404(Muscle, name=muscle_name)
    exercises = Exercise.objects.filter(muscles= muscle)
    return render(request, 'exercises.html', {'exercises': exercises, 'muscle': muscle.name})
def exercise_view(request, exercise_id):
    exercise= get_object_or_404(Exercise, id= exercise_id)
    return render(request, 'exercise.html', {'exercise':exercise})

def nutritional_suplements_view(request):
    nutritional_suplements = NutritionalSuplement.objects.all()
    return render(request, 'nutritional_suplements.html', {'nutritional_suplements': nutritional_suplements})

def suplements_view(request, nutritional_suplement_name):
    nutritional_suplement=get_object_or_404(NutritionalSuplement, name=nutritional_suplement_name)
    suplements = Suplement.objects.filter(nutritional_suplement= nutritional_suplement)
    return render(request, 'suplements.html', {'suplements': suplements, 'nutritional_suplement':nutritional_suplement.name})
def suplement_view(request, suplement_id):
    suplement= get_object_or_404(Suplement, id=suplement_id)
    return render(request, 'suplement.html', {'suplement':suplement})



def index_view(request):
    indice = Manual.objects.all()
    return render(request, 'indice.html', {'indice': indice})





