from django.contrib import admin
from manual.models import Exercise, Muscles, Tag, Suplements, NutritionalSuplements

# Registrar los modelos de la aplicación 'manual'
admin.site.register(Exercise)
admin.site.register(Muscles)
admin.site.register(Tag)
admin.site.register(Suplements)
admin.site.register(NutritionalSuplements)
