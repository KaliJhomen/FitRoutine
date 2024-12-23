from django.contrib import admin
from .models import Exercise, Muscle, NutritionalSuplement, Suplement, Tag

admin.site.register(Muscle)
admin.site.register(Exercise)

admin.site.register(Suplement)
admin.site.register(NutritionalSuplement)
admin.site.register(Tag)