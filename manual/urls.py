from django.urls import path
from . import views
app_name='manual'
urlpatterns = [
    path('exercise/', views.exercises_view, name='exercises'),
    path('nutrition/', views.nutrition_view, name='nutrition'),
    path('encyclopedia/', views.encyclopedia_view, name='encyclopedia'),
]