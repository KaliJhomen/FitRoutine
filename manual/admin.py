from django.contrib import admin
from .models import Exercise, MuscleGroup, NutritionalSuplements, Suplements

admin.site.register(MuscleGroup)
admin.site.register(Exercise)

admin.site.register(Suplements)
admin.site.register(NutritionalSuplements)