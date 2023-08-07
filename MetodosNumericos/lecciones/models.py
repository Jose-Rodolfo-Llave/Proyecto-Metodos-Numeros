from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.TextField()

class Leccion(models.Model):
    titulo = models.TextField()
    descripcion = models.TextField()
    contenido_texto = models.TextField()
    ruta_imagen = models.TextField()
    ruta_recurso = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    status = models.TextField()

class Ejercicio(models.Model):
    enunciado = models.TextField()
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    ruta_imagen = models.TextField()

class Respuesta(models.Model):
    texto_respuesta = models.TextField()
    es_correcta = models.BooleanField()
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)

class Evaluacion(models.Model):
    titulo = models.TextField()
    descripcion = models.TextField()

class EvaluacionEjercicio(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)

class Resultado(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE)

class ProgresoLecciones(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    completada = models.BooleanField()

class Puntuacion(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()