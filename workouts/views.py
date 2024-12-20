from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Workout
from .forms import WorkoutForm

@login_required
def workouts_list(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts.html', {'workouts': workouts})

@login_required
def create_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workouts_list')
    else:
        form = WorkoutForm()
    return render(request, 'create_workout.html', {'form': form})

@login_required
def edit_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workouts_list')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'edit_workout.html', {'form': form, 'workout': workout})

@login_required
def delete_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    if request.method == 'POST':
        workout.delete()
        return redirect('workouts_list')
    return render(request, 'delete_workout.html', {'workout': workout})