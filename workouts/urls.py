from django.urls import path
from . import views
app_name = 'workouts'  
urlpatterns = [
    path('', views.workout_routines, name='workouts_routines'),
    path('create/', views.create_workout_routine, name='create_workout_routine'),
    path('add_exercise/<int:workout_id>/', views.add_workout_exercise, name='add_workout_exercise'),

]