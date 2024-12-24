from django.urls import path
from . import views
app_name = 'workouts'  
urlpatterns = [
    path('routines/', views.workout_routines_view, name='workouts_routines'),
    path('create/', views.create_workout_routine_view, name='create_workout_routine'),
    path('add_exercises/<int:workout_id>/', views.add_workout_exercise_view, name='add_workout_exercise'),
    path('select_muscle/<int:workout_id>/', views.select_muscle_view, name='select_muscle'),
    path('select_exercises/<str:muscle_name>/<int:workout_id>/', views.select_exercises_view, name='select_exercises'),
    path('detail/<int:workout_id>/', views.detail_workout_routine_view, name='detail_workout_routine'),
    path('edit_exercise/<int:exercise_id>/', views.edit_workout_exercise_view, name='edit_workout_exercise'),
    path('delete/<int:workout_id>/', views.delete_workout_routine_view, name='delete_workout_routine'),
]