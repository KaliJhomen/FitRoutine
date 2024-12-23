from django.urls import path
from . import views
app_name='manual'
urlpatterns = [
    path('muscles/', views.muscles_view, name="muscles"),
    path('exercises/<str:muscle_name>/', views.exercises_view, name='exercises'),
    path('exercise/<int:exercise_id>/', views.exercise_view, name='exercise'),
    
    path('nutritional_suplements/', views.nutritional_suplements_view, name='nutritional_suplements'),
    path('suplements<str:nutritional_suplement_name>/', views.suplements_view, name='suplements'),
    path('suplement/<int:suplement_id>', views.suplement_view, name='suplement'),
    
    path('indice/', views.index_view, name='indice'),
]