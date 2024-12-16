from django.contrib import admin
from django.urls import path, include
from .views import base_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('workouts/', include('workouts.urls')),
    path('manual/', include('manual.urls')),
    path('', base_view, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),  # For login, logout, password reset
]