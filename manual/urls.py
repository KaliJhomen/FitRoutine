from django.urls import path
from . import views
app_name='manual'
urlpatterns = [
    path('nutrition/', views.nutrition_view, name='nutrition'),
    path('indice/', views.index_view, name='indice'),
    path('exercises/<str:muscle_group>/', views.exercises_view, name='exercises'),
    path('muscle_groups/', views.muscle_groups_view, name="muscle_groups"),
    path('add_exercise/', views.add_exercise, name='add_exercise'),
]