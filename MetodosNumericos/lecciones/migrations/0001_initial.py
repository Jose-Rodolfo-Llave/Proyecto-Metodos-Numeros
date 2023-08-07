# Generated by Django 3.2.4 on 2023-08-07 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.TextField()),
                ('ruta_imagen', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Leccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('descripcion', models.TextField()),
                ('contenido_texto', models.TextField()),
                ('ruta_imagen', models.TextField()),
                ('ruta_recurso', models.TextField()),
                ('status', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecciones.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_respuesta', models.TextField()),
                ('es_correcta', models.BooleanField()),
                ('ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecciones.ejercicio')),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecciones.respuesta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Puntuacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.IntegerField()),
                ('leccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecciones.leccion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Progreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completada', models.BooleanField()),
                ('leccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecciones.leccion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EvaluacionEjercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ejercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecciones.ejercicio')),
                ('evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecciones.evaluacion')),
            ],
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='leccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecciones.leccion'),
        ),
    ]
