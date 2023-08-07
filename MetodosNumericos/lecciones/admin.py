from django.contrib import admin
from .models import Usuarios, Categorias, Lecciones, Ejercicios, Respuestas, Evaluaciones, EvaluacionesEjercicios, Resultados, ProgresoLecciones, Puntuaciones

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Categorias)
admin.site.register(Lecciones)
admin.site.register(Ejercicios)
admin.site.register(Respuestas)
admin.site.register(Evaluaciones)
admin.site.register(EvaluacionesEjercicios)
admin.site.register(Resultados)
admin.site.register(ProgresoLecciones)
admin.site.register(Puntuaciones)