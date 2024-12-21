from django.contrib import admin
from manual.models import Exercise, MuscleGroup
from users.models import UserProfile
from workouts.models import Workout

# Registrar los modelos de la aplicación 'manual'
admin.site.register(Exercise)
admin.site.register(MuscleGroup)

# Registrar los modelos de la aplicación 'users'
admin.site.register(UserProfile)

# Registrar los modelos de la aplicación 'workouts'
admin.site.register(Workout)