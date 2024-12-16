from django.urls import path
from . import views
app_name = 'workouts'  
urlpatterns = [
    path('', views.workouts_list, name='workouts'),
    path('create/', views.create_workout, name='create_workout'),
    path('edit/<int:id>/', views.edit_workout, name='edit_workout'),
    path('delete/<int:id>/', views.delete_workout, name='delete_workout'),
]