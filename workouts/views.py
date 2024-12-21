from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WorkoutRoutine, WorkoutExercise
from .forms import WorkoutRoutineForm, WorkoutExerciseForm

@login_required
def workout_routines(request):
    routines = WorkoutRoutine.objects.filter(user=request.user).order_by('-date_created')
    return render(request, 'workout_routines.html', {'routines': routines})

@login_required
def create_workout_routine(request):
    if request.method == 'POST':
        form = WorkoutRoutineForm(request.POST)
        if form.is_valid():
            workout_routine = form.save(commit=False)
            workout_routine.user = request.user
            workout_routine.save()
            form.save_m2m()  # Save the many-to-many relationships
            return redirect('workouts:workout_routines')
    else:
        form = WorkoutRoutineForm()
    return render(request, 'create_workout_routine.html', {'form': form})

@login_required
def add_workout_exercise(request, workout_id):
    workout_routine = WorkoutRoutine.objects.get(id=workout_id)
    if request.method == 'POST':
        form = WorkoutExerciseForm(request.POST)
        if form.is_valid():
            workout_exercise = form.save(commit=False)
            workout_exercise.workout = workout_routine
            workout_exercise.save()
            return redirect('workouts:workout_detail', workout_id=workout_id)
    else:
        form = WorkoutExerciseForm()
    return render(request, 'workouts/add_workout_exercise.html', {'form': form, 'workout_routine': workout_routine})