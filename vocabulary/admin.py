from django.contrib import admin
from .models import Word  # Importas tu modelo

# Registras el modelo para que sea visible
admin.site.register(Word)