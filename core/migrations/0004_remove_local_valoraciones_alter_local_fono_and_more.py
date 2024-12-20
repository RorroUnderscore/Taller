# Generated by Django 5.1.1 on 2024-11-20 04:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_local_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='local',
            name='valoraciones',
        ),
        migrations.AlterField(
            model_name='local',
            name='fono',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='local',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='locales_imagenes/'),
        ),
        migrations.RemoveField(
            model_name='local',
            name='imagenes',
        ),
        migrations.AlterField(
            model_name='local',
            name='latitud',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='local',
            name='longitud',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='locales_imagenes/')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_local', to='core.local')),
            ],
        ),
        migrations.CreateModel(
            name='Valoracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.IntegerField()),
                ('comentario', models.TextField()),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valoraciones', to='core.local')),
            ],
        ),
        migrations.AddField(
            model_name='local',
            name='imagenes',
            field=models.ManyToManyField(blank=True, related_name='locales_imagenes', to='core.imagen'),
        ),
    ]
