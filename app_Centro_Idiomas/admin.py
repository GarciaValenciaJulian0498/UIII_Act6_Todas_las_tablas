from django.contrib import admin
from .models import Idioma, Profesor, Clase, Alumnos, Aulas

# Registrar los modelos aquí.
admin.site.register(Idioma)
admin.site.register(Profesor)
admin.site.register(Clase)    # Dejar pendiente
admin.site.register(Alumnos)
admin.site.register(Aulas)