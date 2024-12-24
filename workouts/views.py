from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WorkoutRoutine, WorkoutExercise, Exercise, Muscle
from .forms import WorkoutRoutineForm, WorkoutExerciseForm

@login_required
def workout_routines_view(request):
    routines = WorkoutRoutine.objects.filter(user=request.user).order_by('-date_created')
    return render(request, 'workouts_routines.html', {'routines': routines})

@login_required
def create_workout_routine_view(request):
    if request.method == 'POST':
        routine_name = request.POST.get('routine_name')
        if 'save_routine' in request.POST:
            workout_routine = WorkoutRoutine.objects.create(user=request.user, name=routine_name)
            return redirect('workouts:create_workout_routine')
        elif 'add_exercise' in request.POST:
            workout_routine = WorkoutRoutine.objects.create(user=request.user, name=routine_name)
            request.session['workout_id'] = workout_routine.id
            return redirect('workouts:select_muscle', workout_id=workout_routine.id)
    else:
        workout_routine = None
        exercises = WorkoutExercise.objects.filter(workout_routine__user=request.user)
        return render(request, 'create_workout_routine.html', {'exercises': exercises, 'workout_routine': workout_routine})

@login_required
def select_muscle_view(request, workout_id):
    muscles = Muscle.objects.all()
    return render(request, 'select_muscle.html', {'muscles': muscles, 'workout_id':workout_id})

@login_required
def select_exercises_view(request, muscle_name, workout_id):
    muscle = get_object_or_404(Muscle, name=muscle_name)
    exercises = Exercise.objects.filter(muscles=muscle)
    workout_routine = get_object_or_404(WorkoutRoutine, id=workout_id)

    if request.method == 'POST':
        selected_exercises = request.POST.getlist('exercises')
        for exercise_id in selected_exercises:
            exercise = get_object_or_404(Exercise, id=exercise_id)
            WorkoutExercise.objects.create(workout_routine=workout_routine, exercise=exercise)
        return redirect('workouts:add_workout_exercise', workout_id=workout_routine.id)

    return render(request, 'select_exercises.html', {'exercises': exercises, 'workout_routine': workout_routine})

@login_required
def add_workout_exercise_view(request, workout_id):
    workout_routine = get_object_or_404(WorkoutRoutine, id=workout_id)
    exercises = WorkoutExercise.objects.filter(workout_routine=workout_routine)

    if request.method == 'POST':
        for exercise in exercises:
            sets = request.POST.get(f'sets_{exercise.id}', '0')
            reps = request.POST.get(f'reps_{exercise.id}', '0')
            weight = request.POST.get(f'weight_{exercise.id}', '0')
            exercise.sets = int(sets) if sets else 0
            exercise.reps = int(reps) if reps else 0
            exercise.weight = float(weight) if weight else 0.0
            exercise.save()
        return redirect('workouts:workouts_routines')

    return render(request, 'add_workout_exercise.html', {'workout_routine': workout_routine, 'exercises': exercises})

@login_required
def detail_workout_routine_view(request, workout_id):
    workout_routine = get_object_or_404(WorkoutRoutine, id=workout_id)
    exercises = WorkoutExercise.objects.filter(workout_routine=workout_routine)

    if request.method == 'POST':
        for exercise in exercises:
            sets = request.POST.get(f'sets_{exercise.id}', '0')
            reps = request.POST.get(f'reps_{exercise.id}', '0')
            weight = request.POST.get(f'weight_{exercise.id}', '0')
            exercise.sets = int(sets) if sets else 0
            exercise.reps = int(reps) if reps else 0
            exercise.weight = float(weight) if weight else 0.0
            exercise.save()
        return redirect('workouts:detail_workout_routine', workout_id=workout_routine.id)

    return render(request, 'detail_workout_routine.html', {'workout_routine': workout_routine, 'exercises': exercises})

@login_required
def edit_workout_exercise_view(request, exercise_id):
    exercise = get_object_or_404(WorkoutExercise, id=exercise_id)

    if request.method == 'POST':
        sets = request.POST.get('sets', '0')
        reps = request.POST.get('reps', '0')
        weight = request.POST.get('weight', '0')
        exercise.sets = int(sets) if sets else 0
        exercise.reps = int(reps) if reps else 0
        exercise.weight = float(weight) if weight else 0.0
        exercise.save()
        return redirect('workouts:detail_workout_routine', workout_id=exercise.workout_routine.id)

    return render(request, 'edit_workout_exercise.html', {'exercise': exercise})
@login_required
def delete_workout_routine_view(request, workout_id):
    workout_routine = get_object_or_404(WorkoutRoutine, id=workout_id)
    if request.method == 'POST':
        workout_routine.delete()
        return redirect('workouts:workouts_routines')
    return render(request, 'detail_workout_routine.html', {'workout_routine': workout_routine})