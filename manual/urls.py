from django.urls import path
from . import views
app_name='manual'
urlpatterns = [
    path('muscle_groups/', views.muscle_groups_view, name="muscle_groups"),
    path('exercises/<str:muscle_group_name>/', views.exercises_view, name='exercises'),
    path('nutritional suplements/', views.nutritional_suplements_view, name='nutritional suplements'),
    path('indice/', views.index_view, name='indice'),
]